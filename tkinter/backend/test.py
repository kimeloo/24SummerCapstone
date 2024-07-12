import os, sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from backend.main import connectDB

dbTest = connectDB()

# # SELECT Test
# where = dict()
# where['user_id'] = '1'
# print(dbTest._selectTb('details', ['Sex', 'Bmi', 'Fat'], where, latest=0))

# INSERT Test
data = dict()
data['나이'] = 9
data['성별'] = 'Female'
data['키 (cm)'] = 9
data['체중 (kg)'] = 9
data['체지량지수 (BMI)'] = 9
data['체지방 (Kg)'] = 9
print(data)
## 실제 전화번호 형식은 '-' 없음, test dummy에는 - 존재
(1, 'John Doe', 'john.doe@example.com', '010-1234-5678'),
selectByPhone = dict()
selectByPhone['phone_number'] = '010-1234-5678'
userID = dbTest._selectTb('useraccount', ['ID'], selectByPhone, isWhereDb=False)[0][0]
print(userID)

selectByID = dict()
selectByID['user_id'] = userID
data['user_id'] = userID
print(data)
dbTest._insertTb('details', data)
print(dbTest._selectTb('details', ['*'], selectByID))