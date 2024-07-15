import os, sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from envLoaderServer import loadEnv
SERVER_HOST = loadEnv()

import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
consoleHandler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
consoleHandler.setFormatter(formatter)
logger.addHandler(consoleHandler)

import login as Login
import insertTable as InsertTable
import fetchTable as FetchTable

class ConnectUI():
    '''frontend UI/UX와 연결'''
    def __init__(self):
        self.server = ConnectServer()
    
    def login(self, phone=None, email=None):
        loginStatus = self.server.login(phone=phone, email=email)
        if loginStatus:
            logger.info('Login Success!')
        else:
            logger.error('Login Failed.')

    
    def fromUI(self, table=str(), data=dict()):
        '''frontend에서 호출하여, 데이터를 backend로 전송'''
        logger.debug(f'Fetched data:table={table}\tdata={data}')
        if self.server.toServer(table, data):
            logger.info('Data transmission success!')
        else:
            logger.error('Data transmission failed.')
    
    def toUI(self, table=str(), columns=list()):
        '''frontend에서 호출하여, DB 데이터를 UI로 전송'''
        logger.debug(f'Request data:table={table}\tcolumns={columns}')
        result = self.server.fromServer(table)
        print(result)
        if result!=False:
            logger.info('Data reception success!')
            filteredByCols = {key:result[key] for key in columns if key in result}
            logger.info('Data filtering success!')
            logger.debug(f'Filtered data:table={table}\tdata={filteredByCols}')
            return filteredByCols
        else:
            logger.error('Data reception failed')
            return {'error':'No Data'}

class ConnectServer():
    '''서버 데이터 송수신'''
    def __init__(self):
        self.token = None

    def login(self, phone, email):
        '''서버에 로그인'''
        try:
            loginServer = Login.JwtAuthClient(SERVER_HOST)
            loginServer.login(phone_number=phone, email_address=email)
            self.token = loginServer.get_token()
            return True
        except:
            return False

    def toServer(self, table, data):
        '''서버로 데이터 전송'''
        try:
            insertServer = InsertTable.InsertTable(self.token, SERVER_HOST)
            result = insertServer.insertTable(table, data)
            if 'success' in result:
                return True
        except:
            pass
        return False

    def fromServer(self, table):
        try:
            fetchServer = FetchTable.FetchTable(self.token, SERVER_HOST)
            result = fetchServer.fetchTable(table)
            print(f'Server:{result}')
            if 'error' in result:
                raise
            return result
        except:
            return False
    
# 백엔드 테스트 코드
if __name__ == '__main__':
    # print('Do not run this file directly.')
    backend = ConnectUI()

    ##### Login Test #####
    loginCase = int(input('로그인 테스트 : 전화번호(0), 이메일(1) >> '))
    if loginCase:
        email = 'example@example.com'
        backend.login(email=email)
    else:
        phone = '01012345678'
        backend.login(phone=phone)
    
    ##### fromUI Test #####
    table = 'details'
    data = dict(bmi=123, age=142, sex='Male')
    fromUITest = backend.fromUI(table, data)
    
    ##### toUI Test #####
    table = 'health'
    toUITest = backend.toUI(table=table, columns=['id'])
    print(f'toUI Test : \n{toUITest}')