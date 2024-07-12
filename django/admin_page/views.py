from django.shortcuts import render
from .models import UserAccount, Details, Health, Sensors

def index(request):
    content_list = UserAccount.objects.all()
    # content_list = UserAccount.objects.order_by('-pub_date')[:5] # 역순 정렬(최신 콘텐츠 상단에 노출)
    context = {'content_list': content_list}
    return render(request, 'admin_page/content_list.html', context)
