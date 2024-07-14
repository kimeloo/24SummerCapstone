from django.contrib.auth import login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from admin_page.models import UserAccount
from rest_framework_simplejwt.tokens import AccessToken
import logging

logger = logging.getLogger(__name__)

@csrf_exempt
def LoginView(request):
    if request.method == 'POST':
        phone_num = request.POST.get('phone_num')
        email = request.POST.get('email')
        if not(phone_num or email):
            logger.error(f'User failed to log in. phone_num: {phone_num}, email: {email}')
            return JsonResponse({'error': 'POST phone_num or email'}, status=400)

        # 사용자 검색
        try:
            user = UserAccount.objects.get(phone_num=phone_num, email=email)
        except UserAccount.DoesNotExist:
            user = UserAccount.objects.create(phone_num=phone_num, email=email)
            user.save()

        # JWT 토큰 생성
        access_token = AccessToken.for_user(user)

        # 사용자 로그인 처리
        login(request, user)
        logger.info(f'User {user.id} logged in successfully.')
        return JsonResponse({'ID': user.id, 'token':str(access_token)}, status=200)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)