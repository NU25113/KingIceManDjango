from django.urls import path
from . import views

urlpatterns = [
     path('', views.index,name='index'),
     path('Budget_information/', views.mg_budget,name='mg_budget'),
     path('Cost_information/', views.mg_cost,name='mg_cost'),
     path('Income_information/', views.mg_come,name='mg_come'),
     path('Agency_rent_information/', views.mg_RT_agency,name='mg_RT_agency'),


     path('Ice_bucket_warehouse_information/', views.mg_IB_main,name='mg_IB_main'),
     path('Ice_bucket_fallow_warehouse/', views.mg_IB_fallow,name='mg_IB_fallow'),
     path('Ice_bucket_tracking_information/', views.mg_IB_tracking,name='mg_IB_tracking'),
     path('Ice_bucket_warehouse_lost/', views.mg_IB_lost,name='mg_IB_lost'),
     path('Ice_bucket_warehouse_damaged/', views.mg_IB_damaged,name='mg_IB_damaged'),

     path('Report_Budget_information/', views.rp_budget,name='rp_budget'),
     path('Report_Cost_information/', views.rp_cost,name='rp_cost'),
     path('Report_Income_information/', views.rp_come,name='rp_come'),
     path('Report_Agency_rent_information/', views.rp_a_RT_agency,name='rp_a_RT_agency'),


     path('Report_Ice_bucket_warehouse_information/', views.rp_a_IB_main,name='rp_a_IB_main'),
     path('Report_Ice_bucket_fallow_warehouse/', views.rp_a_IB_fallow,name='rp_a_IB_fallow'),
     path('Report_Ice_bucket_tracking_information/', views.rp_a_IB_tracking,name='rp_a_IB_tracking'),
     path('Report_Ice_bucket_warehouse_lost/', views.rp_a_IB_lost,name='rp_a_IB_lost'),
     path('Report_Ice_bucket_warehouse_damaged/', views.rp_a_IB_damaged,name='rp_a_IB_damaged'),
#################################################?     ADD    ?####################################################
     # path('Create-Budget_information/', views.create_budget,name='create_budget'),
     # path('Update-Budget_information/<int:pk>/', views.update_budget,name='update_budget'),
     # path('Delete-Budget_information/<int:pk>/', views.delete_budget,name='delete_budget'),



]