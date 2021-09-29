from django.urls import path
from django.contrib import admin
from . import views

# from .views import form_login


urlpatterns = [
     path('', views.index,name="index"),
     # path('user_login', views.index,name="user_login"),
     path('login/', views.login,name='login'),
     path('form_login/', views.form_login,name="form_login"),
     path('Sign_In/', views.Sign_In,name="Sign_In"),
     path('register/', views.register,name='register'),
     path('logout', views.logout,name='logout'),

     
] 