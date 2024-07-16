import os
from dotenv import load_dotenv

def loadEnv():
    '''/env/.env 파일에 DB 연결정보 작성, 해당 정보는 .gitignore로 비공개 처리'''
    dotenvPath = os.path.join(os.path.dirname(__file__), '..', '..', 'env', '.env')
    load_dotenv(dotenvPath)

    host = os.getenv('SERVER_HOST')
    return host

if __name__ == '__main__':
    print('Do not run this file directly.')