from django.shortcuts import render
from django.template import Context, Template
from appAdmin.models import Job_queue

from django.db.models import Prefetch
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import auth,User
# Create your views here.
from appMain.decorators import allowed_users,admin_only
from appMain.models import *
from django.http import JsonResponse,HttpResponse
import json
import datetime
from django.urls import reverse
import xlwt
# import StringIO
# from io import StringIO
# import xlsxwriter

# from django.views import View
# import csv
from django.utils import timezone
# from django.template.loader import get_template, render_to_string
# from weasyprint import HTML
# import tempfile
# from django.db.models import Sum


# from io import BytesIO
# from xhtml2pdf import pisa
# import xhtml2pdf.pisa as pisa
###################### Report พนักงาน ###########################
@login_required(login_url="appMain:form_login")
@admin_only
# @allowed_users(allowed_roles=['Ceo'])
def index(request):
    # Budget = Budget.objects.all()
    Ceo = auth.get_user(request)
    job = Job_queue.objects.all()
    context = {
        'Ceo':Ceo,
        'job':job,
        # 'Budget':Budget
    }
    return render(request, 'ceo/index.html',context)

def rp_c_sales(request):
    return render(request, 'ceo/rp_c_sales.html')

def rp_c_accou(request):
    return render(request, 'ceo/rp_c_accou.html')

###################### Report ลูกค้า ###########################

def rp_c_ajen(request):
    Agen = Agency.objects.all()
    context = {
        'Agen':Agen}
    return render(request, 'ceo/rp_c_ajen.html',context)

def rp_c_customer(request):
    custm = Customer.objects.all()
    context = {'custm':custm}
    return render(request, 'ceo/rp_c_customer.html',context)

###################### Report คลังdad ###########################

def rp_c_IB_main(request):
    bmain = bucket_main.objects.all()
    context = {'bmain':bmain}
    return render(request, 'ceo/rp_c_IB_main.html',context)

def rp_c_IB_fallow(request):
    return render(request, 'ceo/rp_c_IB_fallow.html')

def rp_c_IB_tracking(request):
    return render(request, 'ceo/rp_c_IB_tracking.html')

def rp_c_IB_lost(request):
    lost = bucket_lost.objects.all()
    context = {
        'lost':lost,
        }
    return render(request, 'ceo/rp_c_IB_lost.html',context)

def rp_c_IB_damaged(request):
    damaged = bucket_damaged.objects.all()
    context = {
        'damaged':damaged,
        }
    return render(request, 'ceo/rp_c_IB_damaged.html',context)

############################### รายการเช่า #############################################
def rp_c_customer_rent(request):
    cusRen = Customer_rental.objects.all()
    context = {'cusRen':cusRen}
    return render(request, 'ceo/rp_c_customer_rent.html',context)

def rp_c_ajen_rent(request):
    AgencyR = Agency_rent.objects.all()

    # total_price = sum(AgencyR.values_list('quantity', flat=True))
    # if request.user.is_authenticated:
    #     employee = request.user.employee
    #     listt = List.objects.get_or_create(employee=employee, complete=False)
    #     items = listt.agency_rent_set.all()
    # else:
    #     items = []

    # list  = List.objects.all()
    # items = list.Agency_rent_set.all()
    context = {
        'AgencyR':AgencyR, 
        # 'total_price':total_price,
        # 'list':list,
        # # 'bucket':bucket
        # 'items':items,
        }
    return render(request, 'ceo/rp_c_ajen_rent.html',context)


#################################### การเงิน ######################################################
def rp_c_budget(request):
    Budg = Budget.objects.all()

    context = {
        'Budg':Budg,
    }
    return render(request, 'ceo/rp_c_budget.html',context)

# def rp_c_cost(request):
#     cost = Cost.objects.all()
#     Context = {
#         'cost':cost
#     }
#     return render(request,'ceo/rp_c_cost.html',{
#         'cost':cost
#     })

def rp_c_income(request):
    income = Income.objects.all()
    AgenR = Agency_rent.objects.all()
    context = {
        'AgenR':AgenR,
        'income':income,
    }
    return render(request, 'ceo/rp_c_income.html',context)


def export_excel_AR(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Agency_rent'+\
        str(datetime.datetime.now())+'.xls'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Agency_rent')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Bucket main', 'List', 'Quantity','Rental period','Date']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Agency_rent.objects.all().values_list('bucket_main', 'List', 'quantity', 'Rental_period','Date',)
    rows = [[x.strftime("%Y-%m-%d %H:%M") if isinstance(x, datetime.datetime) else x for x in row] for row in rows ]
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response

def export_excel_A(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Agency'+\
        str(datetime.datetime.now())+'.xls'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Agency')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['ID Aj', 'First name', 'Last name', 'Address','Tel','Image']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Agency.objects.all().values_list('ID_Aj', 'F_Agency', 'L_Agency', 'Address','Tel','image')
    rows = [[x.strftime("%Y-%m-%d %H:%M") if isinstance(x, datetime.datetime) else x for x in row] for row in rows ]
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response

def export_excel_C(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Customer'+\
        str(datetime.datetime.now())+'.xls'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Customer')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['ID CT', 'First name', 'Last name', 'Address','Tel']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Customer.objects.all().values_list('ID_cd', 'F_Customer', 'L_Customer', 'Address','Tel')
    rows = [[x.strftime("%Y-%m-%d %H:%M") if isinstance(x, datetime.datetime) else x for x in row] for row in rows ]
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response

def export_excel_CR(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Customer_rental'+\
        str(datetime.datetime.now())+'.xls'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Customer_rental')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['ID bucket', 'List', 'Customer', 'Date','Rental period']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Customer_rental.objects.all().values_list('bucket_main', 'List', 'Customer', 'Date','Rental_period')
    rows = [[x.strftime("%Y-%m-%d %H:%M") if isinstance(x, datetime.datetime) else x for x in row] for row in rows ]
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response

def export_excel_BM(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=bucket_main'+\
        str(datetime.datetime.now())+'.xls'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('bucket_main')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['ID bucket', 'Size', 'Price', 'Note','Date']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = bucket_main.objects.all().values_list('ID_bk', 'sizes', 'price', 'Note','date_added')
    rows = [[x.strftime("%Y-%m-%d %H:%M") if isinstance(x, datetime.datetime) else x for x in row] for row in rows ]
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response

def export_excel_BL(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=bucket_lost' +\
        str(datetime.datetime.now())+'.xls'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('bucket_lost')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Name List','ID Bk' ,'Agency', 'Customer', 'Note','Date']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = bucket_lost.objects.all().values_list('Name_List', 'ID_bk', 'Agency', 'Customer','Note','Date')
    rows = [[x.strftime("%Y-%m-%d %H:%M") if isinstance(x, datetime.datetime) else x for x in row] for row in rows ]
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response

def export_excel_BD(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=bucket_damaged' +\
        str(datetime.datetime.now())+'.xls'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('bucket_damaged')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['ID Bk' ,'Name Recipient', 'Name Sender', 'Quantity','Date','Note']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = bucket_damaged.objects.all().values_list('ID_bk', 'Name_recipient', 'Name_sender','quantity','Date','Note')
    rows = [[x.strftime("%Y-%m-%d %H:%M") if isinstance(x, datetime.datetime) else x for x in row] for row in rows ]
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response

def export_excel_BG(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Budget' +\
        str(datetime.datetime.now())+'.xls'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Budget')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['ID Bg' ,'Name budget', 'Price', 'Staff','Date']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Budget.objects.all().values_list('ID_budget', 'Name_budget', 'price','staff','Date')
    rows = [[x.strftime("%Y-%m-%d %H:%M") if isinstance(x, datetime.datetime) else x for x in row] for row in rows ]
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response

# def export_excel_CS(request):
#     response = HttpResponse(content_type='application/ms-excel')
#     response['Content-Disposition'] = 'attachment; filename=Cost' +\
#         str(datetime.datetime.now())+'.xls'

#     wb = xlwt.Workbook(encoding='utf-8')
#     ws = wb.add_sheet('Cost')

#     # Sheet header, first row
#     row_num = 0

#     font_style = xlwt.XFStyle()
#     font_style.font.bold = True

#     columns = ['ID' ,'Name budget', 'Sum price', 'Staff','Date']

#     for col_num in range(len(columns)):
#         ws.write(row_num, col_num, columns[col_num], font_style)

#     # Sheet body, remaining rows
#     font_style = xlwt.XFStyle()

#     rows = Cost.objects.all().values_list('id', 'Name_budget', 'sum_price','staff','Date')
#     rows = [[x.strftime("%Y-%m-%d %H:%M") if isinstance(x, datetime.datetime) else x for x in row] for row in rows ]
#     for row in rows:
#         row_num += 1
#         for col_num in range(len(row)):
#             ws.write(row_num, col_num, row[col_num], font_style)

#     wb.save(response)
#     return response

def export_excel_IC(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Income' +\
        str(datetime.datetime.now())+'.xls'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Income')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['ID' ,'ID bucket', 'Agency rent', 'Name List','Total Price','Date']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Income.objects.all().values_list('id', 'bucket_main', 'Agency_rent','Name_List','total_price','Date')
    rows = [[x.strftime("%Y-%m-%d %H:%M") if isinstance(x, datetime.datetime) else x for x in row] for row in rows ]
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response