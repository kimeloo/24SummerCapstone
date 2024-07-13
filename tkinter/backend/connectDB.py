from datetime import datetime, timedelta
import mysql.connector
from . import envLoader
from . import varMap

HOST, PORT, USER, PASSWORD, DATABASE = envLoader.loadEnv()          # DB 연결 정보 저장

class ConnectDB():
    '''DB와 연결 및 변수명 조정'''
    def __init__(self):
        '''DB connection'''
        self.db = self._connectDB()             # DB 연결 함수 호출하여 연결 정보를 self.db에 저장
        if self.db == None:                     # DB 연결 실패시 raise로 중단
            print("DB Not Connected\nBye")
            raise ValueError("DB Connection Failed")
        else:
            self.var = varMap.VarMap()          # DB 연결 성공시 UI-DB 변수 매칭을 위해 varMap 호출

    def _connectDB(self):
        '''DB 연결, DB 연결 정보 반환, 실패시 None 반환'''
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
        except mysql.connector.Error as e:      # 연결 실패시 오류 출력 및 None 반환
            print(f"DB connection Error : {e}")
            return None

    def _selectTb(self, table, select=list(), where=dict(), isSelectDb=True, isWhereDb=True, latest=1):
        '''
        DB 변수명 입력이 기본, UI 변수명이라면 isSelectDb=False, isWhereDb=False
        가장 최근 값 하나만을 조회가 기본, latest 값 조절하여 최근 n개 조회, latest=0이면 전체 조회
        SELECT 에러 발생시 None 반환
        '''
        # DB var이 아닌, UI var로 입력된 경우 DB var로 변경
        if not isSelectDb:
            select = self.var.toDbVar(table,dict.fromkeys(select, []))[0]       # toDbVar에는 dict 입력되므로, select list의 값을 key로 갖는 dict 생성
            
        if not isWhereDb:
            where = dict(zip(*self.var.toDbVar(table, where)))                  # where는 dict 형태이므로 바로 toDbVar에 입력

        # SELECT 쿼리 중, WHERE 부분 및 cursor.execute 값 생성
        querySelect = ", ".join(select)                                 # Query에서 SELECT 절에 들어갈 구문 작성
        queryWhere = " and ".join([f'{key} = %s' for key in where])     # Query에서 WHERE 절에 들어갈 구문 작성
        data = [where[key] for key in where]                            # %s에 채울 data 목록 작성

        if latest>0:                                            # latest 값이 0이 아닌 경우, 최근 n개 조회하도록 작성 (default 1)
            orderBy = f"ORDER BY created_time DESC LIMIT {int(latest)}"
        else:                                                   # latest 값이 0인 경우, 모든 값을 조회하도록 작성 
            orderBy = "ORDER BY created_time"
        
        query = f'SELECT {querySelect} FROM {table} WHERE {queryWhere} {orderBy}'
        return self._executeQuery(query, data=data, fetch=True)
        

    def _insertTb(self, table, rawData):
        '''
        table에 INSERT로 삽입
        성공시 True, 실패시 False 반환
        '''
        keys, data = self.var.toDbVar(table, rawData)
        queryColumns = ', '.join(keys)
        queryPlaceholders = ', '.join(['%s']*len(keys))

        query = f'INSERT INTO {table} ({queryColumns}) VALUES ({queryPlaceholders})'
        return self._executeQuery(query, data, fetch=False)
        
    def _updateTb(self, table, rawData, user_id):
        '''
        table에 user_id와 맞는 최신 데이터에 rawData 추가 -> 데이터 업데이트
        '''
        tupleID = self.__canUpdateTb(table, user_id)
        if tupleID == False:    # UPDATE 불가능 판정이므로, INSERT로 입력하도록 False Return
            return False
        keys, data = self.var.toDbVar(table, rawData)
        querySet = ', '.join(f'{key} = %s' for key in keys)
        query = f'UPDATE {table} SET {querySet} WHERE ID = %s'
        data.append(tupleID)

        return self._executeQuery(query, data, fetch=False)     # UPDATE 성공 여부 반환

    def __canUpdateTb(self, table, user_id):
        '''
        useraccount를 제외한 table에서 user_id로 가장 최근 1개 튜플 조회
        조회된 튜플에서, TIMESTAMP 값이 현재 시간으로부터 2시간 이내인 경우 UPDATE 가능
        UPDATE 가능한 경우, 채워넣으려는 값이 조회된 튜플에서 None(빈칸)이어야 하며 이외에는 INSERT
        user_id로 조회한 가장 최근 튜플의 ID를 가져와 return
        '''
        selectResult = self._selectTb(table, select=['ID', 'created_time'], where=dict({'user_id':user_id}))[0]
        try:
            tupleID = selectResult['ID']
            timestamp = selectResult['created_time']
            if (tupleID==None) or (timestamp==None):
                raise Exception('No recent data')
            
            now = datetime.now()
            isMore2H = (now-timestamp) > timedelta(hours=2)
            if isMore2H:     # 너무 오래전 데이터이므로 UPDATE 불가
                raise Exception("No recent data")
            
        except Exception as e:
            tupleID = False
            print(f'DB {table} table UPDATE rejected : {e}')

        finally:
            return tupleID
    
    def _executeQuery(self, query, data=None, fetch=False):
        '''
        Query 실행 부분
        fetch는 기본 False (값 반환 X)
        SELECT의 경우 fetch=True로 지정 필요
        정상 실행된 경우 fetch된 값이나 True 반환, 에러난 경우 None 반환
        '''
        try:
            with self.db.cursor(dictionary=True) as cursor:
                cursor.execute(query, data)
                if fetch:
                    result = cursor.fetchall()              # 쿼리 전송 및 반환값 result에 저장
                else:
                    self.db.commit()                        # 반환값이 없는 쿼리 전송
                    result = True                           # 반환값이 없으므로 result에 True 저장
            return result
        except mysql.connector.Error as e:
            print(f'DB {query[:6]} execute Error : {e}')
            return None                                     # 쿼리 전송 실패하여 None 반환

if __name__ == '__main__':
    print('Do not run this file directly.')