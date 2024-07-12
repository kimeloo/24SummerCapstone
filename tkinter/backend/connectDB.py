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
            select_query = f'SELECT {querySelect} FROM {table} WHERE {queryWhere} {orderBy}'
            cursor.execute(select_query, data)

            result = cursor.fetchall()

            if result:
                result = list(result)
        except mysql.connector.Error as e:
            print(f"DB {table} table select Error : {e}")
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
            insert_query = f'INSERT INTO {table} ({queryColumns}) VALUES ({queryPlaceholders})'
            cursor.execute(insert_query, data[1])
            self.db.commit()
        except mysql.connector.Error as e:
            print(f"DB {table} table insert Error : {e}")
        finally:
            if self.db.is_connected():
                cursor.close()

if __name__ == '__main__':
    print('Do not run this file directly.')