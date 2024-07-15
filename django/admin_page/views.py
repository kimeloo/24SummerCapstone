from django.shortcuts import render
from .models import UserAccount, Details, Health, Sensors, Recommend

def combined_view(request):
    users = UserAccount.objects.all()
    details = Details.objects.all()
    health = Health.objects.all()
    sensors = Sensors.objects.all()
    recommend = Recommend.objects.all()
    context = {
        'users': users,
        'details': details,
        'health': health,
        'sensors': sensors,
        'recommends': recommend
    }
    return render(request, 'admin_page/content_list.html', context)