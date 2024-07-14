# login 로직 (클라이언트에서 jwt를 사용, Django에 연동할 거임, id만을 이용해서)
import requests
import os, sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from envLoaderServer import loadEnv
SERVER_HOST = loadEnv()

class JwtAuthClient:
    def __init__(self, serverUrl):
        self.serverUrl = serverUrl
        self.Endpoint = '/api/login/'
        self.token = None

    # 사용자 ID를 전달하여 로그인 요청을 보냄
    def login(self, phone_number=None, email_address=None):
        data = {
            'phone_num' : phone_number,
            'email' : email_address
        }
        try:
            response = requests.post(self.serverUrl + self.Endpoint, data=data)
            response_data = response.json()
            if response.status_code == 200:
                # 로그인 요청 결과로 받은 JWT 토큰은 클래스 내의 jwt_token 속성에 저장됨
                self.jwt_token = response_data.get('token')
                self.user_id = response_data.get('ID')
                print("로그인 성공!")
            else:
                print("로그인 실패:", response_data.get('message'))

        except requests.exceptions.RequestException as e:
            print("요청 중 오류 발생:", e)

    def get_token(self):
        return self.jwt_token

# 클래스 테스트 코드
if __name__ == "__main__":
    client = JwtAuthClient(SERVER_HOST)
    phone_number = input('전화번호 입력 >> ')
    client.login(phone_number=phone_number)
    print("받은 JWT 토큰 :", client.get_token())