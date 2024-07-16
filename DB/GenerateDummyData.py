import csv
import random
from faker import Faker

class DataGenerator:
    def __init__(self, locale='ko_KR'):
        """
        DataGenerator 클래스의 초기화 메서드입니다.

        Args:
        - locale (str): Faker 라이브러리에서 사용할 지역 설정
        """
        self.fake = Faker(locale)

    def generateSensorsDummyData(self, numRows):
        """
        Sensors 테이블용 더미 데이터를 생성하는 메서드입니다.

        Args:
        - numRows (int): 생성할 데이터 행의 수

        Returns:
        - list of lists: Sensors 테이블에 삽입할 데이터 리스트
        """
        data = []
        for _ in range(numRows):
            user_id = random.randint(1, 100)
            rm01 = random.uniform(0.0, 100.0)
            rm02 = random.uniform(0.0, 100.0)
            rm03 = random.uniform(0.0, 100.0)
            rm04 = random.uniform(0.0, 100.0)
            rm05 = random.uniform(0.0, 100.0)
            rm06 = random.uniform(0.0, 100.0)
            created_time = self.fake.date_time_between(start_date='-1y', end_date='now')
            data.append([user_id, rm01, rm02, rm03, rm04, rm05, rm06, created_time])
        return data

    def exportSensorsToCsv(self, numRows, filename="dummy_sensors_data.csv"):
        """
        Sensors 테이블용 더미 데이터를 생성하고 CSV 파일로 저장하는 메서드입니다.

        Args:
        - numRows (int): 생성할 데이터 행의 수
        - filename (str): 저장할 CSV 파일 이름
        """
        header = ["user_id", "rm01", "rm02", "rm03", "rm04", "rm05", "rm06", "created_time"]
        dummy_data = self.generateSensorsDummyData(numRows)
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerows(dummy_data)
        print(f"Sensors 더미 데이터가 {filename} 파일로 생성되었습니다.")

    def generateHealthDummyData(self, numRows):
        """
        Health 테이블용 더미 데이터를 생성하는 메서드입니다.

        Args:
        - numRows (int): 생성할 데이터 행의 수

        Returns:
        - list of lists: Health 테이블에 삽입할 데이터 리스트
        """
        data = []
        for _ in range(numRows):
            user_id = random.randint(1, 100)
            diabetes_status = random.uniform(0.0, 1.0)
            dyslipidemia_status = random.uniform(0.0, 1.0)
            fatty_liver_status = random.uniform(0.0, 1.0)
            metabolic_syndrome = random.uniform(0.0, 1.0)
            anemia_status = random.uniform(0.0, 1.0)
            hypertension_status = random.uniform(0.0, 1.0)
            obesity_status = random.uniform(0.0, 1.0)
            hypothyroidism_status = random.uniform(0.0, 1.0)
            hyperthyrodism_status = random.uniform(0.0, 1.0)
            created_time = self.fake.date_time_between(start_date='-1y', end_date='now')
            data.append([user_id, diabetes_status, dyslipidemia_status, fatty_liver_status,
                        metabolic_syndrome, anemia_status, hypertension_status, obesity_status,
                        hypothyroidism_status, hyperthyrodism_status, created_time])
        return data

    def exportHealthToCsv(self, numRows, filename="dummy_health_data.csv"):
        """
        Health 테이블용 더미 데이터를 생성하고 CSV 파일로 저장하는 메서드입니다.

        Args:
        - numRows (int): 생성할 데이터 행의 수
        - filename (str): 저장할 CSV 파일 이름
        """
        header = ["user_id", "diabetes_status", "dyslipidemia_status", "fatty_liver_status",
                "metabolic_syndrome", "anemia_status", "hypertension_status", "obesity_status",
                "hypothyroidism_status", "hyperthyrodism_status", "created_time"]
        dummy_data = self.generateHealthDummyData(numRows)
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerows(dummy_data)
        print(f"Health 더미 데이터가 {filename} 파일로 생성되었습니다.")

    def generateDetailsDummyData(self, numRows):
        """
        Details 테이블용 더미 데이터를 생성하는 메서드입니다.

        Args:
        - numRows (int): 생성할 데이터 행의 수

        Returns:
        - list of lists: Details 테이블에 삽입할 데이터 리스트
        """
        data = []
        for _ in range(numRows):
            user_id = random.randint(1, 100)
            sex = random.choice(['Male', 'Female'])
            bmi = random.uniform(15.0, 40.0)
            fat = random.uniform(5.0, 50.0)
            age = random.uniform(18.0, 80.0)
            fat_percentage = random.uniform(5.0, 50.0)
            hr = random.uniform(50.0, 120.0)
            waist = random.uniform(50.0, 120.0)
            whr = random.uniform(0.5, 1.0)
            muscle = random.uniform(20.0, 80.0)
            sbp = random.uniform(80.0, 180.0)
            dbp = random.uniform(50.0, 120.0)
            hdl = random.uniform(30.0, 100.0)
            ldl = random.uniform(50.0, 200.0)
            tg = random.uniform(50.0, 300.0)
            total_chol = random.uniform(120.0, 300.0)
            fg = random.uniform(60.0, 200.0)
            ppg = random.uniform(80.0, 300.0)
            alt = random.uniform(5.0, 200.0)
            hb = random.uniform(10.0, 20.0)
            tsh = random.uniform(0.1, 10.0)
            created_time = self.fake.date_time_between(start_date='-1y', end_date='now')
            height = random.uniform(150.0, 200.0)
            weight = random.uniform(40.0, 150.0)
            data.append([user_id, sex, bmi, fat, age, fat_percentage, hr, waist, whr, muscle,
                         sbp, dbp, hdl, ldl, tg, total_chol, fg, ppg, alt, hb, tsh, created_time, height, weight])
        return data

    def exportDetailsToCsv(self, numRows, filename="dummy_details_data.csv"):
        """
        Details 테이블용 더미 데이터를 생성하고 CSV 파일로 저장하는 메서드입니다.

        Args:
        - numRows (int): 생성할 데이터 행의 수
        - filename (str): 저장할 CSV 파일 이름
        """
        header = ["user_id", "sex", "bmi", "fat", "age", "fat_percentage", "hr", "waist", "whr", "muscle",
                  "sbp", "dbp", "hdl", "ldl", "tg", "total_chol", "fg", "ppg", "alt", "hb", "tsh", "created_time",
                  "height", "weight"]
        dummy_data = self.generateDetailsDummyData(numRows)
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerows(dummy_data)
        print(f"Details 더미 데이터가 {filename} 파일로 생성되었습니다.")

    def generateUseraccountDummyData(self, numRows):
        """
        Useraccount 테이블용 더미 데이터를 생성하는 메서드입니다.

        Args:
        - numRows (int): 생성할 데이터 행의 수

        Returns:
        - list of lists: Useraccount 테이블에 삽입할 데이터 리스트
        """
        data = []
        for _ in range(numRows):
            name = self.fake.name()
            email = self.fake.email()
            phone_num = self.fake.phone_number()
            created_time = self.fake.date_time_between(start_date='-1y', end_date='now')
            is_active = random.choice([0, 1])
            data.append([name, email, phone_num, created_time, is_active])
        return data

    def exportUseraccountToCsv(self, numRows, filename="dummy_useraccount_data.csv"):
        """
        Useraccount 테이블용 더미 데이터를 생성하고 CSV 파일로 저장하는 메서드입니다.

        Args:
        - numRows (int): 생성할 데이터 행의 수
        - filename (str): 저장할 CSV 파일 이름
        """
        header = ["name", "email", "phone_num", "created_time", "is_active"]
        dummy_data = self.generateUseraccountDummyData(numRows)
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerows(dummy_data)
        print(f"Useraccount 더미 데이터가 {filename} 파일로 생성되었습니다.")

# 클래스 사용 예시
if __name__ == "__main__":
    env = 'dummy/'
    generator = DataGenerator()
    generator.exportSensorsToCsv(10, env + "dummy_sensors_data.csv")   # Sensors 테이블에 10개의 더미 데이터 생성
    generator.exportHealthToCsv(10, env + "dummy_health_data.csv")     # Health 테이블에 10개의 더미 데이터 생성
    generator.exportDetailsToCsv(10, env + "dummy_details_data.csv")   # Details 테이블에 10개의 더미 데이터 생성
    generator.exportUseraccountToCsv(5, env + "dummy_useraccount_data.csv")  # Useraccount 테이블에 5개의 더미 데이터 생성
