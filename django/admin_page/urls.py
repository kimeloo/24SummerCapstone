from django.urls import path
from .views import combined_view

urlpatterns = [
    path('', combined_view), #127.0.0.1/admin_page에 들어오면 combined_view함수를 실행.
]