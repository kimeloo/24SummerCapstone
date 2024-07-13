from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Details

# 테스트를 위해 로그 변수 추가
log = []

# 1조 함수 정의
def TeamOne(instance, created, **kwargs):
    if created:
        message = f"TeamOne(signals.py/TeamOne): 새로운 details 객체가 생성되었습니다: {instance}"
    else:
        message = f"TeamOne(signals.py/TeamOne): 기존 details 객체가 업데이트되었습니다: {instance}"
    log.append(message)
    print(message)  # 디버깅을 위해 추가

# 2조 함수 정의
def TeamTwo(instance, created, **kwargs):
    if created:
        message = f"TeamTwo(signals.py/TeamTwo): 새로운 details 객체 생성 시 함수 TeamTwo가 호출되었습니다: {instance}"
    else:
        message = f"TeamTwo(signals.py/TeamTwo): 기존 details 객체 업데이트 시 함수 TeamTwo가 호출되었습니다: {instance}"
    log.append(message)
    print(message)  # 디버깅을 위해 추가

# 시그널 리시버 정의
@receiver(post_save, sender=Details)
def execute_functions(sender, instance, created, **kwargs):
    TeamOne(instance, created)
    TeamTwo(instance, created)
