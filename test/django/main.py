import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from envLoaderServer import loadEnv
SERVER_HOST = loadEnv()
# SERVER_HOST = 'localhost:8000'
import login

def main():
    loginTest = login.JwtAuthClient(SERVER_HOST)
    loginTest.login(phone_number='01012345678')
    token = loginTest.get_token()
    print(token)

if __name__ == "__main__":
    main()