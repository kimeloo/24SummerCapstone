from datetime import datetime, timedelta
import mysql.connector
from . import envLoader
from . import varMap

HOST, PORT, USER, PASSWORD, DATABASE = envLoader.loadEnv()

class connectDB():
    '''DB와 연결 및 변수명 조정'''
    def __init__(self):
        '''DB connection'''
        self.db = self._connectDB()
        if self.db == None:
            print("DB Not Connected")
            print("Bye")
            raise
        else:
            self.var = varMap.varMap()

    def _connectDB(self):
        try:
            connection = mysql.connector.connect(
                host=HOST,
                port=PORT,
                user=USER,
                password=PASSWORD,
                database=DATABASE
            )
            if connection.is_connected():
                print("DB connection Success")
                return connection
        except mysql.connector.Error as e:
            print(f"DB connection Error : {e}")
            return None
    
    def _selectTb(self, table, select=list(), where=dict(), isSelectDb=True, isWhereDb=True, latest=1):
        '''table에서 where 조건으로 select 값 조회, where와 select는 기본 DB var
        기본적으로, created_time 값(DB TIMESTAMP)이 가장 큰 경우 하나만을 조회하도록 설정, latest 값 조절하여 최근 n개 조회'''
        # DB var이 아닌, UI var로 입력된 경우 DB var로 변경
        if not isSelectDb:
            tempSelect = dict()
            for key in select:
                tempSelect[key] = []
            select = self.var.toDbVar(table, tempSelect)[0]
        if not isWhereDb:
            tempWhere = self.var.toDbVar(table, where)
            where = dict()
            for idx, key in enumerate(tempWhere[0]):
                where[key] = tempWhere[1][idx]
            
        # SELECT 쿼리 중, WHERE 부분 및 cursor.execute 값 생성
        whereToString = []
        data = []
        for key in where:
            whereToString.append(f'{key} = %s')
            data.append(where[key])
        queryWhere = " and ".join(whereToString)
        querySelect = ", ".join(select)
        # 가장 최신값 하나만을 조회하도록 설정(default)
        if latest>0:
            orderBy = f"ORDER BY created_time DESC LIMIT {latest}"
        else:
            orderBy = ""
        result = None
        try:
            cursor = self.db.cursor()
            selectQuery = f'SELECT {querySelect} FROM {table} WHERE {queryWhere} {orderBy}'
            cursor.execute(selectQuery, data)
            result = cursor.fetchall()
            if result:
                result = list(result)
        except mysql.connector.Error as e:
            print(f"DB {table} table SELECT Error : {e}")
        finally:
            if self.db.is_connected():
                cursor.close()
        return result

    def _insertTb(self, table, rawData):
        '''_matchVarMap으로 만든 쿼리 바탕으로 table에 INSERT로 삽입'''
        data = self.var.toDbVar(table, rawData)
        # DB 쿼리 작성
        queryColumns = ', '.join(data[0])
        queryPlaceholders = ', '.join(['%s']*len(data[0]))
        try:
            cursor = self.db.cursor()
            insertQuery = f'INSERT INTO {table} ({queryColumns}) VALUES ({queryPlaceholders})'
            cursor.execute(insertQuery, data[1])
            self.db.commit()
        except mysql.connector.Error as e:
            print(f"DB {table} table INSERT Error : {e}")
        finally:
            if self.db.is_connected():
                cursor.close()
    
    def _updateTb(self, table, rawData, user_id):
        tupleID = self.__canUpdateTb(table, user_id)
        if tupleID == False:    # UPDATE 불가능 판정이므로, INSERT로 입력하도록 False Return
            return False
        data = self.var.toDbVar(table, rawData)
        # DB 쿼리 작성
        for idx, key in enumerate(data[0]):
            data[0][idx] = str(key)+' = %s'
        querySet = ', '.join(data[0])
        queryVal = data[1].append(user_id)
        try:
            cursor = self.db.cursor()
            updateQuery = f'UPDATE {table} SET {querySet} WHERE user_id = %s'
            cursor.execute(updateQuery, queryVal)
            self.db.commit()
        except mysql.connector.Error as e:
            print(f'DB {table} table UPDATE Error : {e}')
        finally:
            if self.db.is_connected():
                cursor.close()
        return True             # UPDATE 가능 및 성공이므로, INSERT로 입력할 필요 없도록 True Return

    def __canUpdateTb(self, table, user_id):
        '''useraccount를 제외한 table에서 user_id로 가장 최근 1개 튜플 조회
        조회된 튜플에서, TIMESTAMP 값이 현재 시간으로부터 2시간 이내인 경우 UPDATE 가능
        UPDATE 가능한 경우, 채워넣으려는 값이 조회된 튜플에서 None(빈칸)이어야 하며 이외에는 INSERT
        user_id로 조회한 가장 최근 튜플의 ID를 가져와 return'''
        tupleID = True
        timestamp = None
        try:
            cursor = self.db.cursor()
            selectQuery = f'SELECT * FROM {table} WHERE user_id = %s ORDER BY created_time DESC LIMIT 1'
            cursor.execute(selectQuery, user_id)
            result = cursor.fetchone()
            if result:
                result = result[0]      # [()] 형태의 result를 () 형태로 변환
                columnNames = [desc[0] for desc in cursor.description]      # table 내 컬럼명 저장
                for idx, column in enumerate(columnNames):
                    if column == 'ID':      # UPDATE할 튜플의 ID를 tupleID에 저장
                        tupleID = result[idx]
                    if column == 'created_time':
                        timestamp = result[idx]
                if timestamp == None:
                    print(f'updateTb Error : No Timestamp')
                    raise Exception("No Timestamp")
            else:
                raise Exception("No result")
            now = datetime.now()
            isMore2H = (now-timestamp) > timedelta(hours=2)
            if isMore2H:     # UPDATE 가능
                raise Exception("No recent data")

        except mysql.connector.Error as e:
            tupleID = False
            print(f'DB {table} table SELECT Error : {e}')
        except Exception as e:
            tupleID = False
            print(f'DB {table} table UPDATE rejected : {e}')
        finally:
            if self.db.is_connected():
                cursor.close()
        return tupleID

if __name__ == '__main__':
    print('Do not run this file directly.')