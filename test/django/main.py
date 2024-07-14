import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from envLoaderServer import loadEnv
SERVER_HOST = loadEnv()
# SERVER_HOST = 'localhost:8000'
import login
import fetchTable
# import insertTable


def main():
    ###### login Test ######
    phone_number = '01012345678'
    print(f'login Test : phone_number={phone_number}')
    loginTest = login.JwtAuthClient(SERVER_HOST)
    loginTest.login(phone_number=phone_number)
    token = loginTest.get_token()
    print(f'token : {token}')

    ###### fetchTable Test ######
    table = 'Details'
    print(f'fetchTable Test : table={table}')
    fetchTableTest = fetchTable.FetchTable(token, SERVER_HOST)
    print(fetchTableTest.fetchTable(table))

    # ###### insertTable Test ######
    # table = 'Details'
    # data = dict(BMI=1234)
    # print(f'insertTable Test : table={table}, data={data}')
    # insertTableTest = insertTable.InsertTable(token, SERVER_HOST)
    # print(insertTableTest.insertTable(table, data))

if __name__ == "__main__":
    main()