from . import connectDB

class connectUI():
    '''frontend UI/UX와 연결'''
    def __init__(self):
        self.db = connectDB.connectDB()
    
    def getValue(self, key, value):
        print(f'{key} : {value}')

    def buttonOnClick(self, _from):
        print(f'buttonOnClick from {_from}')

class handler():
    '''frontend에서 넘어온 데이터 처리 및 요구 데이터 반환'''
    def __init__(self):
        self.user_id = None
    
    

    # def 

if __name__ == '__main__':
    print('Do not run this file directly.')