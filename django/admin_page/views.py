from django.shortcuts import render
from .models import UserAccount, Details, Health, Sensors, Recommend

def combined_view(request):
    users = UserAccount.objects.all().reverse()[:5]
    details = Details.objects.all().reverse()[:5]
    health = Health.objects.all().reverse()[:5]
    sensors = Sensors.objects.all().reverse()[:5]
    recommend = Recommend.objects.all().reverse()[:5]
    context = {
        'users': users,
        'details': details,
        'health': health,
        'sensors': sensors,
        'recommends': recommend
    }
    return render(request, 'admin_page/content_list.html', context)