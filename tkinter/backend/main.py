import requests
import os, sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from envLoaderServer import loadEnv
SERVER_HOST = loadEnv()

# frontend 데이터 backend로 전송

class ConnectUI():
    '''frontend UI/UX와 연결'''
    def __init__(self):
        '''Server 연결'''
        self.server = ConnectServer()
    
    def sendDataToBackend(self, data):
        '''frontend에서 호출하여, 데이터를 backend로 전송'''
        try:
            # JSON 형식으로 backend로 데이터 전송
            response = requests.post(SERVER_HOST, json=data) # URL 넣기 - 백엔드 서버의 엔드포인트로
            if response.status_code == 200:
                print("데이터 전송 성공!")
            else:
                print(f"데이터 전송 실패: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print("요청 중 오류 발생:", e)
        
    def getValue(self, key, value):
        '''frontend에서 호출하여, 변수명과 값을 backend로 전달'''
        print(f'{key} : {value}')
    
    def buttonOnClick(self, which, _from):
        '''frontend에서 호출하여, 버튼의 기능과 페이지 위치를 backend로 전달'''
        data = {
            'button': which, # 버튼의 이름
            'from': _from # 클릭이 발생한 위치
        }
        print(f'{which} buttonOnClick from {_from}')
        self.sendDataToBackend(data)

class ConnectServer():
    '''frontend에서 넘어온 데이터 처리 및 요구 데이터 반환'''
    def __init__(self):
        pass
    
    
# 백엔드 테스트 코드
if __name__ == '__main__':
    print('Do not run this file directly.')
    
    ui_connector = ConnectUI()
    ui_connector.buttonOnClick('submit', 'homepage')