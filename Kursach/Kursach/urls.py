"""Kursach URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from firstapp.views import *
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PageHome.as_view()),
    path('home.html', PageHome.as_view()),
    path('index.html', PageIndex.as_view()),
    path('registration.html', PageRegistration.as_view()),
    path('login.html', PageLogin.as_view()),
    path('dogovor.html', PageDogovor.as_view()),
    path('home_emploeer.html', PageHomeEmpoyeer.as_view()),
]
