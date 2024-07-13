# login 로직 (클라이언트에서 jwt를 사용, Django에 연동할 거임, id만을 이용해서)

import requests
import os, sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from envLoaderServer import loadEnv
SERVER_HOST = loadEnv()

class JwtAuthClient:
    def __init__(self, server_url):
        self.server_url = server_url
        self.login_endpoint = '/api/login/'
        self.jwt_token = None

    # 사용자 ID를 전달하여 로그인 요청을 보냄
    def login(self, user_id):
        data = {
            'id': user_id
        }

        try:
            response = requests.post(self.server_url + self.login_endpoint, json=data)
            response_data = response.json()

            if response.status_code == 200:
                # 로그인 요청 결과로 받은 JWT 토큰은 클래스 내의 jwt_token 속성에 저장됨
                self.jwt_token = response_data.get('token') # 여기에 토큰을 입력
                self.user_id = response_data.get('ID') # 여기에 ID를 입력
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
    client.login('1')
    # 현재 저장된 JWT 토큰 가져옴
    token = client.get_token()
    print("받은 JWT 토큰 :", token)
