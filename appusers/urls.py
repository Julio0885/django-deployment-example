from django.contrib import admin
from django.urls import path
from appusers import views

# TEMPLATE URLS!
app_name = 'appusers'

urlpatterns = [
    path('register/',views.register,name='register'),
    path('user_login/',views.user_login,name='user_login'),
    
]
