from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
     path('', views.index,name='index'),
     path('Manage_Sales/', views.rp_c_sales,name='rp_c_sales'),
     path('Manage_Accounting/', views.rp_c_accou,name='rp_c_accou'),
     path('Ajency/', views.rp_c_ajen,name='rp_c_ajen'),
     path('Customer/', views.rp_c_customer,name='rp_c_customer'),
     path('Rental-Ajency/', views.rp_c_ajen_rent,name='rp_c_ajen_rent'),
     path('Rental-Customer/', views.rp_c_customer_rent,name='rp_c_customer_rent'),

     path('Ice_bucket_warehouse_information/', views.rp_c_IB_main,name='rp_c_IB_main'),
     path('Ice_bucket_fallow_warehouse/', views.rp_c_IB_fallow,name='rp_c_IB_fallow'),
     path('Ice_bucket_tracking_information/', views.rp_c_IB_tracking,name='rp_c_IB_tracking'),
     path('Ice_bucket_warehouse_lost/', views.rp_c_IB_lost,name='rp_c_IB_lost'),
     path('Ice_bucket_warehouse_damaged/', views.rp_c_IB_damaged,name='rp_c_IB_damaged'),
     path('Budget/', views.rp_c_budget,name='rp_c_budget'),
     # path('Cost/', views.rp_c_cost,name='rp_c_cost'),
     path('Income/', views.rp_c_income,name='rp_c_income'),

     # path('export-CSV', views.export_CSV,name='export_CSV'),
     # path('export-PDF', views.export_pdf,name='export_pdf'),
     path('Export-Excel-Agency-rent', views.export_excel_AR,name='export_excel_AR'),
     path('Export-Excel-Agency', views.export_excel_A,name='export_excel_A'),
     path('Export-Excel-Customer', views.export_excel_C,name='export_excel_C'),
     path('Export-Excel-Customer-rent', views.export_excel_CR,name='export_excel_CR'),
     path('Export-Excel-Bucket-Main', views.export_excel_BM,name='export_excel_BM'),
     path('Export-Excel-Bucket-Lost', views.export_excel_BL,name='export_excel_BL'),
     path('Export-Excel-Bucket-Damaged', views.export_excel_BD,name='export_excel_BD'),
     path('Export-Excel-Budget', views.export_excel_BG,name='export_excel_BG'),
     # path('Export-Excel-Cost', views.export_excel_CS,name='export_excel_CS'),
     path('Export-Excel-InCome', views.export_excel_IC,name='export_excel_IC'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)