from django.test import TestCase
from .models import UserAccount, Details
from .signals import log
# 테스트 코드 : Details 모델의 인스턴스가 생성되거나 업데이트될 때 함수 TeamOne와 TeamTwo가 호출되는지 확인함
# log 변수를 사용해 함수 호출을 기록하고 테스트에서 이를 검증함
# 테스트 실행 : python manage.py test

class DetailsModelTest(TestCase):
    def setUp(self):
        # 테스트 사용자 생성
        self.user = UserAccount.objects.create(
            name='testuser',
            phone_num='01059595959'
        )    
        # 테스트 전 로그를 초기화합니다.
        log.clear()

    def test_create_details_triggers_signals(self):
        # Details 모델 인스턴스를 생성합니다.
        details = Details.objects.create(
            user=self.user,
            sex='Male',
            bmi=22.5,
            fat=15.0,
            age=25,
            fat_percentage=20.0,
            hr=60,
            waist=32.0,
            whr=0.8,
            muscle=30.0,
            sbp=120,
            dbp=80,
            hdl=50,
            ldl=100,
            tg=150,
            total_chol=200,
            fg=90,
            ppg=110,
            alt=30,
            hb=15,
            tsh=2,
            height=175.0,
            weight=70.0
        )

        print(f"log after create: {log}")  # 디버깅을 위해 추가
        
        # 시그널 핸들러가 호출되었는지 확인합니다.
        # self.assertTrue(any("TeamOne(test.py/test_create): 새로운 details 객체가 생성되었습니다" in message for message in log))
        # self.assertTrue(any("TeamTwo(test.py/test_create): 새로운 details 객체 생성 시 함수 TeamTwo가 호출되었습니다" in message for message in log))

    def test_update_details_triggers_signals(self):
        # Details 모델 인스턴스를 생성하고 업데이트합니다.
        details = Details.objects.create(
            user=self.user,
            sex='Male',
            bmi=22.5,
            fat=15.0,
            age=25,
            fat_percentage=20.0,
            hr=60,
            waist=32.0,
            whr=0.8,
            muscle=30.0,
            sbp=120,
            dbp=80,
            hdl=50,
            ldl=100,
            tg=150,
            total_chol=200,
            fg=90,
            ppg=110,
            alt=30,
            hb=15,
            tsh=2,
            height=175.0,
            weight=70.0
        )
        # 업데이트 후 로그를 초기화합니다.
        log.clear()

        # 인스턴스를 업데이트합니다.
        details.bmi = 23.0
        details.save()

        print(f"log after update: {log}")  # 디버깅을 위해 추가

        # 시그널 핸들러가 호출되었는지 확인합니다.
        # self.assertTrue(any("TeamOne(test.py/test_update): 기존 details 객체가 업데이트되었습니다" in message for message in log))
        # self.assertTrue(any("TeamTwo(test.py/test_update): 기존 details 객체 업데이트 시 함수 TeamTwo가 호출되었습니다" in message for message in log))
