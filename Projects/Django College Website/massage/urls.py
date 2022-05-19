"""hello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from massage import views

urlpatterns = [
   
    path('', views.index,name='index'),
    path('service', views.service,name='service'),
    path('contact', views.contact,name='contact'),
    path('about', views.about,name='about'),
    path('civil', views.civil,name='civil'),
    path('electrical', views.electrical,name='electrical'),
    path('mechanical', views.mechanical,name='mechanical'),
    path('electronics', views.electronics,name='electronics'),
    path('first_year', views.first_year,name='first_year'),
    path('second_year', views.second_year,name='second_year')

]

