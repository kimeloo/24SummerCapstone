# login 로직 (클라이언트에서 jwt를 사용, Django에 연동할 거임, id만을 이용해서)
import requests
import os, sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from envLoaderServer import loadEnv
SERVER_HOST = loadEnv()

class Email:
    def __init__(self, token, serverUrl):
        self.serverUrl = serverUrl
        self.Endpoint = '/api/email/'
        self.headers = {
        'Authorization' : f'Bearer {token}'
        }

    def email(self):
        url = self.serverUrl+self.Endpoint
        try:
            response = requests.get(url, headers=self.headers)
            # response_data = response.json()
            if response.status_code == 200:
                return True
            elif response.status_code == 401:
                return 401
            else:
                return False

        except requests.exceptions.RequestException as e:
            return False

# 클래스 테스트 코드
if __name__ == "__main__":
    token = input('토큰 입력 >> ')
    email = Email(token, SERVER_HOST)
    print(email.email())