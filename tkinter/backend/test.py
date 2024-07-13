import os, sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

# from backend.main import connectUI
from backend.connectDB import ConnectDB

dbTest = ConnectDB()

##### SELECT Test #####
where = dict()
where['user_id'] = '1'
print(dbTest._selectTb('details', ['Sex', 'Bmi', 'Fat'], where, latest=1))

##### INSERT Test #####
data = dict()
input_data = list(input('data 입력\n 성별, 키, 체중, 체질량지수, 체지방, user_id >>').split())
keys = ['성별', '키 (cm)', '체중 (kg)', '체지량지수 (BMI)', '체지방 (Kg)', 'user_id']
for key, val in zip(keys, input_data):
    data[key] = val
print('\n입력 데이터 : ')
print(data)
# (1, 'John Doe', 'john.doe@example.com', '01012345678'),
selectByPhone = dict()

selectByPhone['phone_number'] = input('phone_number 입력 >> ')
userID = dbTest._selectTb('useraccount', ['ID'], selectByPhone, isWhereDb=False)[0]['ID']
print('\nuserID : ')
print(userID)

selectByID = dict()
selectByID['user_id'] = userID
data['user_id'] = userID
# print(data)
dbTest._insertTb('details', data)
print('\n입력 후 조회된 데이터 : ')
print(dbTest._selectTb('details', ['*'], selectByID))

input()
##### UPDATE Test #####
data = dict()
input_data = list(input('data 입력\n 나이, 성별, 키, 체중, 체질량지수, 체지방 >>').split())
keys = ['나이', '성별', '키 (cm)', '체중 (kg)', '체지량지수 (BMI)', '체지방 (Kg)']
for key, val in zip(keys, input_data):
    data[key] = val
print('\n입력 데이터 : ')
print(data)
# (1, 'John Doe', 'john.doe@example.com', '01012345678'),
selectByPhone = dict()

selectByPhone['phone_number'] = input('phone_number 입력 >> ')
userID = dbTest._selectTb('useraccount', ['ID'], selectByPhone, isWhereDb=False)[0]['ID']
print('\nuserID : ')
print(userID)

print(f'UPDATE success : {dbTest._updateTb("details", data, userID)}')
