from django.contrib import admin
from .models import UserAccount, Details, Health, Sensors

admin.site.register(UserAccount)
admin.site.register(Details)
admin.site.register(Health)
admin.site.register(Sensors)