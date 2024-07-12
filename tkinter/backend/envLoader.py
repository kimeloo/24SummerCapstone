import os
from dotenv import load_dotenv

def loadEnv():
    dotenvPath = os.path.join(os.path.dirname(__file__), '..', '..', 'env', '.env')
    load_dotenv(dotenvPath)

    host = os.getenv('DB_HOST')
    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')
    database = os.getenv('DB_NAME')
    return host, user, password, database

if __name__ == '__main__':
    print('Do not run this file directly.')