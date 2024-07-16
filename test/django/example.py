import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from envLoaderServer import loadEnv
SERVER_HOST = loadEnv()
import login
import fetchTable
import insertTable

fromUIvalues = dict()

## UI에서 실행하는 함수 : 변수명과 값을 입력하면 fromUIvalues에 저장됨
## UI에서 import해와서 그 안에서 이 함수를 호출해야함
def fromUI(table, name, value):
    fromUIvalues[name] = (table, value)

def main():
    ###### login Test ######
    phone_number = None
    email = None
    if 'phone_num' in fromUIvalues:
        phone_number = fromUIvalues['phone_num'][1]
    elif 'email' in fromUIvalues:
        email = fromUIvalues['email'][1]
    
    print(f'login Test : phone_number={phone_number}')
    loginTest = login.JwtAuthClient(SERVER_HOST)
    loginTest.login(phone_number=phone_number, email_address=email)
    token = loginTest.get_token()
    print(f'token : {token}')

    ###### insertTable Test : 7, 8번 측정 프로그램의 입력값이 DB로 들어감######
    # fromUIvalues = {'bmi':('details', '23.4'), 'fat':('details', '25')}
    data = dict() # =={}
    keys=['bmi', 'fat'] # == {'bmi':'', 'fat':''}
    for key in keys:
        table = fromUIvalues[key][0] # == 'details' (0번째 반복), == 'details' (1번째 반복)
        value = fromUIvalues[key][1] # == '23.4' , == '25'
        data[key] = value # == {'bmi' : 23.4, 'fat':25}
    print(f'insertTable Test : table={table}, data={data}') # table == details, data는 딕셔너리 형태로
    insertTableTest = insertTable.InsertTable(token, SERVER_HOST) # 서버 연결
    print(insertTableTest.insertTable(table, data)) # 서버 전송 결과 확인

    ###### fetchTable Test ######
    table = 'Details'
    print(f'fetchTable Test : table={table}')
    fetchTableTest = fetchTable.FetchTable(token, SERVER_HOST)
    print(fetchTableTest.fetchTable(table))



if __name__ == "__main__":
    main()