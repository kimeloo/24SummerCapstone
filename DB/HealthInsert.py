import pandas as pd
import mysql.connector
import sys, os
# 현재 파일의 디렉토리 경로
current_dir = os.path.dirname(os.path.abspath(__file__))

# CSV 파일의 상대 경로
csv_file_path = os.path.join(current_dir, 'csv', 'dummy_health_data.csv')

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from envLoaderDB import loadEnv

# 환경 변수 로드
MYDB_HOST, MYDB_PORT, MYDB_USER, MYDB_PW, MYDB_DATABASE = loadEnv()
import mysql.connector

# MySQL 연결 설정
mydb = mysql.connector.connect(
    host=MYDB_HOST,
    port=MYDB_PORT,
    user=MYDB_USER,
    password=MYDB_PW,
    database=MYDB_DATABASE
)

# 커서 생성
mycursor = mydb.cursor()

# 삽입할 데이터
data = [
    (7, 0.6, 0.5, 0.1, 0.7, 0.4, 0.5, 0.8, 0.3, 0.9),
    (8, 0.6, 0.5, 0.8, 0.1, 0.1, 0.3, 0.2, 0.8, 0.9),
    (9, 0.8, 0.5, 0.9, 0.2, 0.4, 0.6, 0.6, 0.2, 0.8),
    (10, 0.3, 0.9, 0.1, 0.4, 0.3, 0.2, 0.1, 1.0, 0.9),
    (7, 0.6, 0.7, 0.4, 0.9, 0.5, 0.5, 0.0, 0.1, 0.7),
    (8, 0.1, 0.6, 0.3, 0.8, 0.9, 0.1, 0.3, 0.9, 0.7),
    (9, 0.5, 0.1, 0.2, 0.9, 0.3, 0.9, 0.1, 0.4, 0.9),
    (10, 0.4, 0.5, 0.5, 0.4, 0.5, 0.7, 0.4, 0.6, 0.1),
    (9, 0.6, 0.5, 0.6, 0.4, 1.0, 1.0, 0.9, 0.3, 0.9),
    (10, 0.9, 0.2, 1.0, 0.5, 0.7, 0.8, 0.0, 0.9, 0.6)
]

# 데이터베이스에 데이터 삽입
sql = "INSERT INTO health (user_id, diabetes_status, dyslipidemia_status, fatty_liver_status, metabolic_syndrome, " \
    "anemia_status, hypertension_status, obesity_status, hypothyroidism_status, hyperthyrodism_status, created_time) " \
    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, NOW())"
mycursor.executemany(sql, data)

# 변경사항 커밋
mydb.commit()

# 연결 종료
mydb.close()
