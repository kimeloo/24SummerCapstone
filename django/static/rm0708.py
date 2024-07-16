### ver1. 240716_171400
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
import random
import mysql.connector
from mysql.connector import Error
from contextlib import contextmanager
import logging
import os

from capstone_project.my_settings import DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, DB_NAME

## 로깅 설정 : 애플리케이션의 실행 중 발생하는 다양한 이벤트를 기록
## 디버깅 및 문제 해결 용이

# 환경 변수 LOG_LEVEL을 읽어옵니다. 만약 환경 변수 LOG_LEVEL이 설정되어 있지 않으면 기본값으로 'INFO'를 사용
# 가져온 문자열을 모두 대문자로 변환합니다. 이는 logging 모듈에서 로깅 레벨이 대문자로 정의되어 있기 때문
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO').upper()

# logging 모듈의 기본 설정을 구성하는 함수입니다. 이 함수는 로깅 시스템을 초기화하고 기본 로거의 설정을 정의
# level=LOG_LEVEL:로깅 레벨을 설정합니다. 여기서는 앞에서 정의한 LOG_LEVEL 값을 사용합니다. 로깅 레벨은 로깅 메시지의 심각도(threshold)를 결정합니다. 설정된 레벨 이상의 심각도를 가진 메시지만 기록됩니다. 로깅 레벨의 계층 구조는 다음과 같습니다:
# DEBUG: 상세한 디버깅 정보
# INFO: 일반 정보
# WARNING: 경고 메시지
# ERROR: 에러 메시지
# CRITICAL: 치명적인 에러
# %(asctime)s: 로그가 기록된 시간 (타임스탬프)
# %(levelname)s: 로그 레벨 이름 (예: DEBUG, INFO, WARNING, ERROR, CRITICAL)
# %(message)s: 실제 로그 메시지
logging.basicConfig(level=LOG_LEVEL, format='%(asctime)s - %(levelname)s - %(message)s') 

## 환경 변수에서 데이터베이스 접속 정보 가져오기

# 환경 변수 'DB_HOST'를 읽어와서 DB_HOST 변수에 저장
# 만약 'DB_HOST' 환경 변수가 설정되어 있지 않으면 기본값으로 'localhost'를 사용
# 'localhost'는 데이터베이스가 로컬 컴퓨터에서 실행 중임을 의미합니다.
#DB_HOST = os.getenv('DB_HOST', 'localhost')

# 환경 변수 'DB_USER'를 읽어와서 DB_USER 변수에 저장합니다.
# 만약 'DB_USER' 환경 변수가 설정되어 있지 않으면 기본값으로 'root'를 사용합니다.
# 'root'는 MySQL의 기본 관리자 계정입니다.
#DB_USER = os.getenv('DB_USER', 'root')

# 환경 변수 'DB_PASSWORD'를 읽어와서 DB_PASSWORD 변수에 저장합니다.
# 만약 'DB_PASSWORD' 환경 변수가 설정되어 있지 않으면 기본값으로 'kghs4404'를 사용합니다.
# 데이터베이스 접근을 위한 비밀번호입니다.
#DB_PASSWORD = os.getenv('DB_PASSWORD', 'kghs4404')

# 환경 변수 'DB_NAME'을 읽어와서 DB_NAME 변수에 저장합니다.
# 만약 'DB_NAME' 환경 변수가 설정되어 있지 않으면 기본값으로 'testdb'를 사용합니다.
# 'testdb'는 데이터베이스의 이름입니다.
#DB_NAME = os.getenv('DB_NAME', 'testdb')

# 환경 변수 'DB_CHARSET'을 읽어와서 DB_CHARSET 변수에 저장합니다.
# 만약 'DB_CHARSET' 환경 변수가 설정되어 있지 않으면 기본값으로 'utf8mb4'를 사용합니다.
# 'utf8mb4'는 유니코드 문자를 지원하는 문자 집합입니다.
#DB_CHARSET = os.getenv('DB_CHARSET', 'utf8mb4')

DB_CHARSET = os.getenv('DB_CHARSET', 'utf8mb4')

## MySQL 데이터베이스 연결을 관리

@contextmanager
def mysql_connection(host=DB_HOST, port=DB_PORT, user=DB_USER, password=DB_PASSWORD, db=DB_NAME):
    connection = None
    try:
        logging.info(f"Connecting to MySQL server at {host} with user {user}")
        connection = mysql.connector.connect(host=host, port=port, user=user, password=password, database=db)
        yield connection
    except mysql.connector.InterfaceError as e:
        logging.error(f"Interface error: {e}")
        raise
    except mysql.connector.DatabaseError as e:
        logging.error(f"Database error: {e}")
        raise
    except mysql.connector.OperationalError as e:
        logging.error(f"Operational error: {e}")
        raise
    except mysql.connector.ProgrammingError as e:
        logging.error(f"Programming error: {e}")
        raise
    except mysql.connector.IntegrityError as e:
        logging.error(f"Integrity error: {e}")
        raise
    except mysql.connector.DataError as e:
        logging.error(f"Data error: {e}")
        raise
    except mysql.connector.NotSupportedError as e:
        logging.error(f"Not supported error: {e}")
        raise
    except Error as e:
        logging.error(f"MySQL에 연결하는 중 오류 발생: {e}")
        raise
    finally:
        if connection:
            connection.close()#특정 사용자 ID에 대한 데이터를 가져온다
def get_user_data(connection, user_id):
    try:
        with connection.cursor(dictionary=True) as cur:
            query = "SELECT * FROM details WHERE user_id = %s ORDER BY created_time DESC LIMIT 1;"
            cur.execute(query, (user_id,))
            result = cur.fetchone()
            if not result:
                logging.warning(f"사용자 ID에 대한 데이터를 찾을 수 없습니다: {user_id}")
            return result
    except mysql.connector.ProgrammingError as e:
        logging.error(f"Programming error while fetching user data: {e}")
        return None
    except mysql.connector.DataError as e:
        logging.error(f"Data error while fetching user data: {e}")
        return None
    except Error as e:
        logging.error(f"사용자 데이터를 검색하는 중 오류 발생: {e}")
        return None


## 사용자의 건강 점수를 계산한다.
def calculate_health_scores(data):


    # 필수 필드 목록 정의
    # 사용자의 건강 데이터를 평가하기 위해 필요한 모든 필드를 포함
    required_fields = ['Sbp', 'Dbp', 'Bmi', 'Fg', 'Ppg', 'Ldl', 'Hdl', 'Tg', 'Total_chol', 'Alt', 'Sex', 'Waist', 'Hb', 'Tsh']
    
    # 필수 필드 중 누락된 필드를 확인
    # required_fields 목록을 순회하여 data 딕셔너리에 없는 필드를 찾아 missing_fields 리스트에 저장합니다.
    missing_fields = [field for field in required_fields if field not in data]

    # 리스트가 비어 있지 않은 경우, 즉 필수 필드 중 누락된 필드가 있는 경우 실행됩니다.
    if missing_fields:

        # 누락된 필드가 있는 경우 오류 로그를 기록하고 None 반환
        logging.error(f"필수 필드가 없습니다: {missing_fields}")
        return None
    
    try: #예외 처리를 위해 사용

        # 값이 None일 경우 기본값을 설정
        data = {k: (v if v is not None else 0) for k, v in data.items()}
        
        # 건강 점수를 저장할 딕셔너리 초기화
        scores = {}
        
        # 각 건강 상태를 평가하여 점수 계산
        scores['고혈압'] = check_hypertension(data['Sbp'], data['Dbp'])
        scores['비만'] = check_obesity(data['Bmi'])
        scores['당뇨병'] = check_diabetes(data['Fg'], data['Ppg'])
        scores['이상지질혈증'] = check_dyslipidemia(data['Ldl'], data['Hdl'], data['Tg'], data['Total_chol'])
        scores['지방간'] = check_fatty_liver(data['Alt'], data['Sex'])
        scores['대사증후군'], scores['metabolic_percent'] = check_metabolic_syndrome(data['Fg'], data['Sex'], data['Waist'], data['Sbp'], data['Dbp'], data['Hdl'], data['Tg'])
        scores['빈혈'] = check_anemia(data['Hb'], data['Sex'])
        scores['갑상선기능저하증'] = check_hypothyroidism(data['Tsh'])
        scores['갑상선기능항진증'] = check_hyperthyrodism(data['Tsh'])

        # 점수가 None인 경우 0으로 변환
        for key in scores:
            if scores[key] is None:
                scores[key] = 0

        
        # 계산된 점수 반환
        return scores
    
    except KeyError as e:
        # 입력 데이터에서 누락된 키가 있는 경우 오류 로그를 기록하고 None 반환
        logging.error(f"입력 데이터 누락: {e}")
        return None


# 고혈압 여부를 판단
def check_hypertension(sbp, dbp):
    if sbp < 120 and dbp < 80:
        return 0
    elif sbp < 140 or dbp < 90:
        return 0.5
    else:
        return 1

# 비만 여부를 판단
def check_obesity(bmi):
    if bmi <= 24.9:
        return 0
    elif 25 <= bmi:
        return 1

# 당뇨병 여부를 판단
def check_diabetes(fasting_glucose, postprandial_glucose):
    if fasting_glucose <= 110 and postprandial_glucose <= 140:
        return 0
    elif (fasting_glucose > 110 and fasting_glucose < 126) or (postprandial_glucose > 140 and postprandial_glucose < 200):
        return 0.5
    elif fasting_glucose >= 126 or postprandial_glucose >= 200:
        return 1

# 이상지질혈증 여부를 판단
def check_dyslipidemia(ldl, hdl, tg, total_chol):
    if ldl >= 130 or hdl < 60 and hdl>0 or tg >= 150 or total_chol >= 200:
        return 1
    else:
        return 0

# 지방간 여부를 판단
def check_fatty_liver(alt, sex):
    if sex == 'Male':
        return 0 if alt <= 40 else 1
    elif sex == 'Female':
        return 0 if alt <= 35 else 1

# 빈혈 여부를 판단
def check_anemia(hb, sex):
    if sex == 'Male':
        return 0 if hb >= 13 else 1
    elif sex == 'Female':
        return 0 if hb >= 12 else 1

# 갑상선기능저하증 여부를 판단
def check_hypothyroidism(tsh):
    if tsh >= 4.0:
        return 1
    else:
        return 0

# 갑상선기능항진증 여부를 판단
def check_hyperthyrodism(tsh):
    if tsh <= 0.4 and tsh > 0:
        return 1
    else:
        return 0

# 대사증후군 여부를 판단
def check_metabolic_syndrome(fg, sex, waist, sbp, dbp, hdl, tg):
    count = 0
    if fg >= 100:
        count += 1
    if (sex == 'Male' and waist >= 90) or (sex == 'Female' and waist >= 80):
        count += 1
    if sbp >= 130 or dbp >= 85:
        count += 1
    if (sex == 'Male' and hdl < 40) or (sex == 'Female' and hdl < 50):
        count += 1
    if tg >= 150:
        count += 1
    return (1, (count / 5) * 100) if count >= 3 else (0, (count / 5) * 100)

# 추천문구를 가져옴
def get_recommendations(connection, disease_code):
 
    try: # 예외 처리를 위해 사용됩니다.
        # SQL 쿼리를 실행하여 recommendation 테이블에서 모든 데이터를 가져옴
        df = pd.read_sql_query("SELECT * FROM recommend", connection)
        
        # 데이터프레임이 비어 있는지 확인
        if df.empty:
            # 비어 있다면 경고 로그를 기록하고 None 반환
            logging.warning("데이터베이스에서 추천문구를 찾을 수 없습니다")
            return None, None, None

        # LabelEncoder 객체를 생성하여 질병 코드를 인코딩
        le_disease = LabelEncoder()

        # 질병 코드를 인코딩하여 새로운 컬럼 disease_encoded에 저장합니다.
        df['disease_encoded'] = le_disease.fit_transform(df['code'])
        
        # 입력 변수(X)와 출력 변수(y) 정의
        X = df[['disease_encoded']]
        y = df['recommendation']
        y_2nd = df['recommendation3']

        # DecisionTreeClassifier 모델을 생성하여 아침과 점심 추천 문구 학습
        model_morning_lunch = DecisionTreeClassifier()
        model_morning_lunch.fit(X, y)

        # DecisionTreeClassifier 모델을 생성하여 저녁 추천 문구 학습
        model_evening = DecisionTreeClassifier()
        model_evening.fit(X, y_2nd)

        # 주어진 질병 코드를 인코딩
        user_disease_encoded = le_disease.transform([disease_code])[0]

        # 인코딩된 질병 코드로 데이터프레임을 생성
        user_input = pd.DataFrame([[user_disease_encoded]], columns=['disease_encoded'])

        # 학습된 모델을 사용하여 아침과 점심 추천 문구의 인덱스를 예측
        recommendation_indices_morning_lunch = model_morning_lunch.apply(user_input)

        # 예측된 인덱스를 사용하여 아침과 점심 추천 문구 목록을 가져옵니다.
        recommendations_morning_lunch = df.iloc[model_morning_lunch.apply(X) == recommendation_indices_morning_lunch[0]]['recommendation'].tolist()

        # 학습된 모델을 사용하여 저녁 추천 문구의 인덱스를 예측
        recommendation_indices_evening = model_evening.apply(user_input)

        # 예측된 인덱스를 사용하여 저녁 추천 문구 목록을 가져옵니다.
        recommendations_evening = df.iloc[model_evening.apply(X) == recommendation_indices_evening[0]]['recommendation3'].tolist()

        # 추천 문구가 없을 경우 경고 로그를 기록하고 None 반환
        if not recommendations_morning_lunch or not recommendations_evening:
            logging.warning("일치하는 추천문구를 찾을 수 없습니다.")
            return None, None, None

        # 추천 문구 중에서 무작위로 하나를 선택
        morning_recommendation = random.choice(recommendations_morning_lunch)
        lunch_recommendation = random.choice(recommendations_morning_lunch)
        evening_recommendation = random.choice(recommendations_evening)

        # 아침, 점심, 저녁 추천 문구 반환
        return morning_recommendation, lunch_recommendation, evening_recommendation
    except Exception as e:
        # 예외 발생 시 오류 로그를 기록하고 None 반환
        logging.error(f"추천문구를 검색하는 도중 오류가 발생: {e}")
        return None, None, None

def update_latest_details_bulk(connection, user_id, updates):
    for field, value in updates.items():
        SQL = f'''
            UPDATE capstonedb.details
            SET {field} = %s
            WHERE id = (
                SELECT id FROM (
                    SELECT id FROM capstonedb.details 
                    WHERE user_id = %s 
                    ORDER BY created_time DESC 
                    LIMIT 1
                ) AS subquery
            );
        '''
        try:
            with connection.cursor() as cur:
                cur.execute(SQL, (value, user_id))
            connection.commit()
        except mysql.connector.ProgrammingError as e:
            logging.error(f"Programming error while updating {field}: {e}")
        except mysql.connector.DataError as e:
            logging.error(f"Data error while updating {field}: {e}")
        except Error as e:
            logging.error(f"Error updating {field}: {e}")

def main(user_id=10):
    with mysql_connection() as connection:
        data = get_user_data(connection, user_id)

        if not data:
            logging.info("해당 ID를 가진 데이터를 찾을 수 없습니다.")
            return

        scores = calculate_health_scores(data)
        
        if scores is None:
            logging.info("건강 점수를 계산할 수 없습니다.")
            return

        health_messages = []
        for condition, status in scores.items():
            if status == 1:
                health_messages.append(f"{condition}에 대한 관리가 필요합니다.")
            elif status == 0.5:
                health_messages.append(f"{condition} 위험군입니다. 관리가 필요합니다.")
            elif status == 0:
                health_messages.append(" ")

        logging.info("\n".join(health_messages))
        logging.info(f"대사증후군이 있을 확률: {scores['metabolic_percent']}%")
        
        re = round(((9 - (scores.get('갑상선기능항진증', 0) + scores.get('이상지질혈증', 0) + 
                          scores.get('지방간', 0) + scores.get('비만', 0) + 
                          scores.get('갑상선기능저하증', 0) + scores.get('고혈압', 0) + 
                          scores.get('당뇨병', 0) + scores.get('빈혈', 0))) / 9) * 100)
        logging.info(f"당신의 건강점수: {re}점")

        disease_code = calculate_disease_code(scores)
        
        morning_recommendation, lunch_recommendation, evening_recommendation = get_recommendations(connection, disease_code)

        logging.info(f"아침: {morning_recommendation}")
        logging.info(f"점심: {lunch_recommendation}")
        logging.info(f"저녁: {evening_recommendation}")

        SQL1 = ''' 
            INSERT INTO capstonedb.health
            (user_id, diabetes_status, dyslipidemia_status, fatty_liver_status, metabolic_syndrome, anemia_status, hypertension_status, obesity_status, hypothyroidism_status, hyperthyrodism_status)
            VALUES
            (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        '''
        try:
            with connection.cursor() as cur:
                cur.execute(SQL1, (data['user_id'], scores['당뇨병'], scores['이상지질혈증'], scores['지방간'], scores['대사증후군'], scores['빈혈'], scores['고혈압'], scores['비만'], scores['갑상선기능저하증'], scores['갑상선기능항진증']))
            connection.commit()
        except Error as e:
            logging.error(f"Error inserting results: {e}")

        updates = {
            'Recommendation1': morning_recommendation,
            'Recommendation2': lunch_recommendation,
            'Recommendation3': evening_recommendation,
            'metabolicper': scores['metabolic_percent'],
            'bodypoint': re
        }
        update_latest_details_bulk(connection, user_id, updates)
        return health_messages

def calculate_disease_code(scores):
    measurement_list = [scores['갑상선기능항진증'], scores['이상지질혈증'], scores['지방간'], scores['비만'], scores['갑상선기능저하증'], scores['고혈압'], scores['당뇨병'], scores['빈혈']]

    counts = sum(1 for score in measurement_list if score >= 0.5)

    if counts == 1:
        for i, score in enumerate(measurement_list):
            if score >= 1:
                return i + 1
    elif counts >= 2:
        return 9

    return 0

if __name__ == "__main__":
    main()
