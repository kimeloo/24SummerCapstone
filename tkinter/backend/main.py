from . import connectDB

class ConnectUI():
    '''frontend UI/UX와 연결'''
    def __init__(self):
        self.db = connectDB.ConnectDB()     # DB 커넥션 우선 확인
    
    def getValue(self, key, value):
        '''frontend에서 호출하여, 변수명과 값을 backend로 전달'''
        print(f'{key} : {value}')

    def buttonOnClick(self, which, _from):
        '''frontend에서 호출하여, 버튼의 기능과 페이지 위치를 backend로 전달'''
        print(f'{which} buttonOnClick from {_from}')

class Handler():
    '''frontend에서 넘어온 데이터 처리 및 요구 데이터 반환'''
    def __init__(self):
        self.user_id = None                 # user_id 값을 저장하여 DB 상호작용에서 활용
    
    

if __name__ == '__main__':
    print('Do not run this file directly.')