import mysql.connector
from . import envLoader

host, port, user, password, database = envLoader.loadEnv()

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
            self._variableMap()

    def _connectDB(self):
        try:
            connection = mysql.connector.connect(
                host=host,
                port=port,
                user=user,
                password=password,
                database=database
            )
            if connection.is_connected():
                print("DB connection Success")
                return connection
        except mysql.connector.Error as e:
            print(f"DB connection Error : {e}")
            return None
    
    def _variableMap(self):
        self.varMapDetailsTb = self.__createVarMapDetailsTb()
        self.varMapUseraccountTb = self.__createVarMapUseraccountTb()

    def _toDbVar(self, table, rawData):
        # UI 변수명을 DB 변수명으로 매핑 : 1. 매핑 테이블 지정
        if table == 'details':
            varMap = self.varMapDetailsTb
        elif table == 'useraccount':
            varMap = self.varMapUseraccountTb
        # UI 변수명을 DB 변수명으로 매핑 : rawData(dict)의 key를 varMap에서 찾아, varMap[key]의 value를 새로운 key로 하고, rawData[key]의 value를 새로운 value로 하는 dict 생성
        data = [[], []]
        for key in rawData:
            data[0].append(varMap[key])
            data[1].append(rawData[key])
        return data
    
    def _selectTb(self, table, select=list(), where=dict(), isSelectDb=True, isWhereDb=True, latest=1):
        '''table에서 where 조건으로 select 값 조회, where와 select는 기본 DB var
        기본적으로, created_time 값(DB TIMESTAMP)이 가장 큰 경우 하나만을 조회하도록 설정, latest 값 조절하여 최근 n개 조회'''
        # DB var이 아닌, UI var로 입력된 경우 DB var로 변경
        if not isSelectDb:
            tempSelect = dict()
            for key in select:
                tempSelect[key] = []
            select = self._toDbVar(table, tempSelect)[0]
        if not isWhereDb:
            tempWhere = self._toDbVar(table, where)
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
        data = self._toDbVar(table, rawData)
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
    
    def __createVarMapUseraccountTb(self):
        # 3page : phone_number or email_address
        varMapKeys = ['phone_number', 'email_address', 'user_id']
        varMapVals = ['phone_num', 'email', 'ID']

        return self.__matchVarMap(varMapKeys, varMapVals)

    def __createVarMapDetailsTb(self):
        '''details Table에 대해, UI 변수명과 DB 변수명 매칭'''
        # default keys
        varMapKeys = ['user_id', 'ID']
        varMapVals = ['user_id', 'user_id']
        # 5page(7) : physical measurements
        varMapKeys.extend(['나이', '성별', '키 (cm)', '체중 (kg)', '체지량지수 (BMI)', 
                           '체지방 (Kg)', '체지방률 (%)', '심장박동수 (bpm)', '허리둘레 (cm)', '골반과 허리둘레 (WHR)', 
                           '근육량 (kg)', '수축기 혈압 (SBP)', '이완기 혈압 (DBP)'])
        varMapVals.extend(['Age', 'Sex', 'Height', 'Weight', 'Bmi',
                           'Fat', 'Fat_percentage', 'Hr', 'Waist', 'Whr',
                           'Muscle', 'Sbp', 'Dbp'])
        # 5page(8) : blood tests
        varMapKeys.extend(['저밀도콜레스테롤(LDL)', '고밀도콜레스테롤(HDL)', '중성지방(TG)', '알라닌아미노전이효소(ALT)', '헤모글로빈(Hb)', 
                                '갑상선자극호르몬(TSH)', '공복혈당(FG)', '식후2시간혈당(PPG)'])
        varMapVals.extend(['Ldl', 'Hdl', 'Tg', 'Alt', 'Hb',
                           'Tsh', 'Fg', 'Ppg'])
        
        return self.__matchVarMap(varMapKeys, varMapVals)

    def __matchVarMap(self, varMapKeys, varMapVals):
        # Match varMap
        _varMapMatched = dict()
        for key, value in zip(varMapKeys, varMapVals):
            _varMapMatched[key] = value
        return _varMapMatched
    

if __name__ == '__main__':
    print('Do not run this file directly.')