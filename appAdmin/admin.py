from django.contrib import admin
from MainDjango.settings import *
from .models import Job_queue
from appMain.models import *
from django.urls import reverse
# from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.
class ManageUser(admin.ModelAdmin):
    list_display = ['First_name', 'Last_name', 'User_Type', 'Tel', 'Address','Username','show_image']
    search_fields = ['First_name', 'User_Type']

class ManageJob(admin.ModelAdmin):
    list_display = ['title', 'queue', 'created', 'updated']
    search_fields = ['title', 'updated']

admin.site.register(Job_queue,ManageJob)
# *=====================================================??=====================================================================


class Manage_Agency(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['ID_Aj','F_Agency','L_Agency','Address','Tel','show_image']

class Manage_List(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['ID_List','Name_List','Agency','Customer','complete','date_add']
    search_fields = ['ID_List', 'Name_List','date_add']

class Manage_Customer(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['ID_cd','F_Customer','L_Customer','Address','Tel']
    search_fields = ['ID_cd', 'Customer']

class Manage_Agency_rent(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['bucket_main','List','quantity','Rental_period','Date',]
    search_fields = ['id', 'List']


admin.site.register(employee)
admin.site.register(Agency,Manage_Agency)
admin.site.register(List,Manage_List)
admin.site.register(Customer,Manage_Customer)
admin.site.register(Agency_rent,Manage_Agency_rent)
# *==================================================== ฝ่าย บัญชี =================================================================
class Manage_bucket_main(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['ID_bk','sizes','price','Note','date_added']


# class Manageclass_tb_Ice_bucket_tracking_information(admin.ModelAdmin):
#     list_display = ['id','Name_List','ID_bk','Note','Date']


class Manageclass_bucket_lost(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['Name_List','ID_bk','Agency','Customer','Note','Date']

class Manageclass_bucket_damaged(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['ID_bk','Name_recipient','Name_sender','quantity','Date','Note']

class Manageclass_Income(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id','bucket_main','Agency_rent','Name_List','total_price','Date']

class Manageclass_Budget(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['ID_budget','Name_budget','price','staff','Date']


class Manageclass_Cost(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id','Name_budget','price','staff','Date']



admin.site.register(bucket_main,Manage_bucket_main)
# admin.site.register(bucket_tracking)
admin.site.register(bucket_lost,Manageclass_bucket_lost)
admin.site.register(bucket_damaged,Manageclass_bucket_damaged)
admin.site.register(Income,Manageclass_Income)
admin.site.register(Budget,Manageclass_Budget)
# admin.site.register(Cost,Manageclass_Cost)

# ? ===========================================================================================
class Manageclass_Customer_rental(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['bucket_main','List','Customer','Rental_period','Date']




admin.site.register(Customer_rental,Manageclass_Customer_rental)

# admin.site.register(tb_Ice_bucket_balance_information)
# admin.site.register(tb_user,ManageUser)
