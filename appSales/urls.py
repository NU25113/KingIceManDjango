from django.urls import path
from . import views

urlpatterns = [
     path('', views.index,name='index'),
     path('Agency_rental_information/', views.mg_RT_ajen,name='mg_RT_ajen'),
     path('Customer_rental_information/', views.mg_RT_costo,name='mg_RT_costo'),
     path('Ice_bucket_balance_information/', views.mg_SK_balance,name='mg_SK_balance'),
     path('Report_Agency_rental_information/', views.rp_s_RT_ajen,name='rp_s_RT_ajen'),
     path('Report_Customer_rental_information/', views.rp_s_RT_costo,name='rp_s_RT_costo'),
     path('Report_Ice_bucket_balance_information/', views.rp_s_SK_balance,name='rp_s_SK_balance'),
     # path('index', views.login,name='index'),mg_RT_ajen
]