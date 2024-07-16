# login 로직 (클라이언트에서 jwt를 사용, Django에 연동할 거임, id만을 이용해서)
import os, sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from envLoaderServer import loadEnv
SERVER_HOST = loadEnv()
import requests

class FetchTable:
    def __init__(self, token, serverUrl):
        self.serverUrl = serverUrl
        self.headers = {
        'Authorization': f'Bearer {token}'
        }

    def fetchTable(self, table):
        self.Endpoint = f'/fetch/select/{table}/'
        url = self.serverUrl+self.Endpoint

        response = requests.post(url, headers=self.headers)
        if response.status_code == 401:
            return 401
        return response.json()

if __name__ == '__main__':
    token = input('토큰 입력 >> ')
    table = input('테이블 입력 >> ')
    table = FetchTable(token, SERVER_HOST)
    print(table.fetchTable(table))