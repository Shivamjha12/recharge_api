from django.contrib import admin
from django.urls import path, include
from Accounts import views 
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

urlpatterns = [
    path('signup/', views.UserRegistration.as_view(), name='signup'),
    path('login', views.login, name='user_login'),
]