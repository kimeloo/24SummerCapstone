class connectUI():
    def __init__(self):
        print("Init")
    
    def getValue(self, key, value):
        print(f'{key} : {value}')

    def buttonOnClick(self, _from):
        print(f'buttonOnClick from {_from}')
    
class toDB():
    def __init__(self):
        '''DB connection'''
    
    

if __name__ == '__main__':
    print("Do not run this file directly.")