from . import connectDB

class connectUI():
    '''frontend UI/UX와 연결'''
    def __init__(self):
        self.db = connectDB.connectDB()
    
    def getValue(self, key, value):
        print(f'{key} : {value}')

    def buttonOnClick(self, _from):
        print(f'buttonOnClick from {_from}')

if __name__ == '__main__':
    print('Do not run this file directly.')