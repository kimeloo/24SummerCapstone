import pandas as pd
import mysql.connector
import sys, os
# 현재 파일의 디렉토리 경로
current_dir = os.path.dirname(os.path.abspath(__file__))

# CSV 파일의 상대 경로
csv_file_path = os.path.join(current_dir, 'csv', 'dummy_useraccount_data.csv')

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from envLoaderDB import loadEnv

# 환경 변수 로드
MYDB_HOST, MYDB_PORT, MYDB_USER, MYDB_PW, MYDB_DATABASE = loadEnv()

class RecommendDataInserter:
    def __init__(self, host, port, user, password, database):
        """
        클래스 초기화 메서드.
        데이터베이스 연결 설정을 초기화합니다.
        """
        self.connection = None
        self.cursor = None
        self.connection = mysql.connector.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database
        )


    def insertData(self, csv_file_path):
        """
        CSV 데이터의 각 행을 테이블에 삽입합니다.
        """
        self._cursorInit()
        df = self._loadCsvData(csv_file_path)
        insert_query = """
        INSERT INTO useraccount (name, email, phone_num, created_time, is_active)
        VALUES (%s, %s, %s, NOW(), %s)
        """
        # 각 행을 반복하면서 데이터 삽입
        for _, row in df.iterrows():
            self.cursor.execute(insert_query, (
                row['name'], row['email'], row['phone_num'], row['is_active'],
            ))
        # 변경사항 커밋
        self.connection.commit()
        self._closeConnection()
        

    def _cursorInit(self):
        """
        커서를 초기화합니다.
        """
        self.cursor = self.connection.cursor()

    def _loadCsvData(self, csv_file_path):
        """
        CSV 파일을 pandas DataFrame으로 읽어옵니다.
        """
        return pd.read_csv(csv_file_path)

    def _closeConnection(self):
        """
        데이터베이스 연결과 커서를 종료합니다.
        """
        if self.cursor:
            self.cursor.close() # 커서 종료
        if self.connection:
            self.connection.close() # 데이터베이스 연결 종료


if __name__ == '__main__':
    # 사용 예시
    inserter = RecommendDataInserter(
        host=MYDB_HOST,      # 데이터베이스 호스트
        port=MYDB_PORT,      # 데이터베이스 포트
        user=MYDB_USER,    # 데이터베이스 사용자
        password=MYDB_PW,# 데이터베이스 비밀번호
        database=MYDB_DATABASE,# 데이터베이스 이름
    )
    # print(f"Host: {inserter.host}, User: {inserter.user}, Password: {inserter.password}, Database: {inserter.database}, CSV File Path: {inserter.csv_file_path}")

    inserter.insertData(csv_file_path) # 데이터 삽입 실행