"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('home.urls')), # 홈 url 설정
    path('polls/', include('polls.urls')), # 설문조사 url 설정
    path('bookmark/', include('bookmark.urls')), # 북마크 url 설정
    path('blog/', include('blog.urls')), # 블로그 url 설정
    path('admin/', admin.site.urls),

]
