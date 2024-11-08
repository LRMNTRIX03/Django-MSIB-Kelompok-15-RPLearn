# UserWeb/urls.py
from django.urls import path
from . import views

app_name = 'UserWeb' 

urlpatterns = [
    path('dashboard', views.index, name='user.dashboard'),
    path('about', views.about, name='user.about'),
    path('kategoriback', views.kategoriBack, name='user.kategoriback'),
    path('kategoriFront', views.kategoriFront, name='user.kategoriFront'),
]
