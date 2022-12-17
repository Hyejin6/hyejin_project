from django.urls import path
from .import views

app_name = 'home' # 네임 스페이스 설정

urlpatterns=[
    path('', views.HomeView.as_view(), name='home'),
]