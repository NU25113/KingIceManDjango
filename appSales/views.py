from django.shortcuts import render
from appAdmin.models import Job_queue
# from appMain.models import tb_Agency_rental_information
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import auth
from appMain.decorators import allowed_users,admin_only


@login_required(login_url="appMain:form_login")
# @allowed_users(allowed_roles=['Sales'])
@admin_only
def index(request):
    
    sales = auth.get_user(request)
    data=Job_queue.objects.all()
    return render(request, 'sales/index.html',{
        'job':data,
        'sales':sales
        })
########################### จัดการ การเช่า ################################
def mg_RT_ajen(request):
    sales = auth.get_user(request)
    # Agency = tb_Agency_rental_information.objects.all()
    return render(request, 'sales/mg_RT_ajen.html',{
        'sales':sales,
        # 'Agency' :Agency
        })
    
def mg_RT_costo(request):
    sales = auth.get_user(request)
    return render(request, 'sales/mg_RT_costo.html',{
        'sales':sales
        })


########################## จัดการยอดคงเหลือ #################################
def mg_SK_balance(request):
    sales = auth.get_user(request)
    return render(request, 'sales/mg_SK_balance.html',{
        'sales':sales
        })


########################### รายงาน การเช่า ################################
def rp_s_RT_ajen(request):
    sales = auth.get_user(request)
    return render(request, 'sales/rp_s_RT_ajen.html',{
        'sales':sales
        })

def rp_s_RT_costo(request):
    sales = auth.get_user(request)
    return render(request, 'sales/rp_s_RT_costo.html',{
        'sales':sales
        })


########################## รายงาน ยอดคงเหลือ #################################
def rp_s_SK_balance(request):
    sales = auth.get_user(request)
    return render(request, 'sales/rp_s_SK_balance.html',{
        'sales':sales
        })
# Create your views here.
