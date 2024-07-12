import os, sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from backend.main import connectDB

dbTest = connectDB()
where = dict()
where['user_id'] = '1'
print(dbTest._selectTb('details', ['Sex', 'Bmi', 'Fat'], where, latest=0))
