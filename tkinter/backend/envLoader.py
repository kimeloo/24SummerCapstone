import os
from dotenv import load_dotenv

def loadEnv():
    dotenvPath = os.path.join(os.path.dirname(__file__), '..', '..', 'env', '.env')
    load_dotenv(dotenvPath)

    host = os.getenv('DB_HOST')
    port = os.getenv('DB_PORT')
    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')
    database = os.getenv('DB_NAME')
    return host, port, user, password, database

if __name__ == '__main__':
    print('Do not run this file directly.')