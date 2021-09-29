from django.shortcuts import render,redirect
from appAdmin.models import Job_queue
from appMain.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import auth,Group
# from .forms import BudgetForm


from appMain.decorators import allowed_users,admin_only

@login_required(login_url="appMain:form_login")
@admin_only
# @allowed_users(allowed_roles=['Accounting'])
def index(request):
    Acc = auth.get_user(request)
    data=Job_queue.objects.all()
    return render(request, 'Accou/index.html',{
        'job':data,
        'Acc':Acc,
        
        })
# Create your views here.
##########################? Manage การเงิน ###############################
@login_required(login_url="appMain:form_login")
def mg_budget(request):
    Acc = auth.get_user(request)
    # Budget_information = tb_Budget_information.objects.all()
    return render(request, 'Accou/mg_budget.html',{
        # 'Budget_information':Budget_information,
        'Acc':Acc,
    })

@login_required(login_url="appMain:form_login")
def mg_cost(request):
    Acc = auth.get_user(request)                
    # Cost_information = tb_Cost_information.objects.all()
    return render(request, 'Accou/mg_cost.html',{
        # 'Cost_information':Cost_information,
        'Acc':Acc,
    })

@login_required(login_url="appMain:form_login")
def mg_come(request):
    Acc = auth.get_user(request)
    # Income_information = tb_Income_information.objects.all()
    return render(request, 'Accou/mg_come.html',{
        # 'Income_information':Income_information,
        'Acc':Acc,
    })

##########################? Manage การเช่า ###############################

@login_required(login_url="appMain:form_login")
@allowed_users(allowed_roles=['admin'])
def mg_RT_agency(request):
    Acc = auth.get_user(request)
    # Agency_rent = tb_Agency_rent_informationd.objects.all()
    return render(request, 'Accou/mg_RT_agency.html',{
        # 'Agency_rent':Agency_rent,
        'Acc':Acc,
    })


##########################? Manage คลังถังน้ำแข็ง ###############################
@login_required(login_url="appMain:form_login")
@allowed_users(allowed_roles=['admin'])
def mg_IB_main(request):
    Acc = auth.get_user(request)
    # warehouse_information = tb_Ice_bucket_warehouse_information.objects.all()
    return render(request, 'Accou/mg_IB_main.html',{
        # 'warehouse_information':warehouse_information,
        'Acc':Acc,
    })


@login_required(login_url="appMain:form_login")
@allowed_users(allowed_roles=['admin'])
def mg_IB_fallow(request):
    Acc = auth.get_user(request)
    # fallow_warehouse = tb_Ice_bucket_fallow_warehouse.objects.all()
    return render(request, 'Accou/mg_IB_fallow.html',{
        # 'fallow_warehouse':fallow_warehouse,
        'Acc':Acc,
    })


@login_required(login_url="appMain:form_login")
@allowed_users(allowed_roles=['admin'])
def mg_IB_tracking(request):
    Acc = auth.get_user(request)
    # tracking_information = tb_Ice_bucket_tracking_information.objects.all()
    return render(request, 'Accou/mg_IB_tracking.html',{
        # 'tracking_information':tracking_information,
        'Acc':Acc,
    })


@login_required(login_url="appMain:form_login")
@allowed_users(allowed_roles=['admin'])
def mg_IB_lost(request):
    Acc = auth.get_user(request)
    # warehouse_lost = tb_Ice_bucket_warehouse_lost.objects.all()
    return render(request, 'Accou/mg_IB_lost.html',{
        # 'warehouse_lost':warehouse_lost,
        'Acc':Acc,
    })


@login_required(login_url="appMain:form_login")
@allowed_users(allowed_roles=['admin'])
def mg_IB_damaged(request):
    Acc = auth.get_user(request)
    # warehouse_damaged = tb_Ice_bucket_warehouse_damaged.objects.all()
    return render(request, 'Accou/mg_IB_damaged.html',{
        # 'warehouse_damaged':warehouse_damaged,
        'Acc':Acc,
    })


##########################? Report การเงิน ###############################
def rp_budget(request):
    Acc = auth.get_user(request)
    # Budget_information = tb_Budget_information.objects.all()
    return render(request, 'Accou/rp_budget.html',{
        # 'Budget_information':Budget_information,
        'Acc':Acc,
    })
def rp_cost(request):
    Acc = auth.get_user(request)
    # Cost_information = tb_Cost_information.objects.all()
    return render(request, 'Accou/rp_cost.html',{
        # 'Cost_information':Cost_information,
        'Acc':Acc,
    })

def rp_come(request):
    Acc = auth.get_user(request)
    # Income_information = tb_Income_information.objects.all()
    return render(request, 'Accou/rp_come.html',{
        # 'Income_information':Income_information,
        'Acc':Acc,
    })

def rp_a_RT_agency(request):
    Acc = auth.get_user(request)
    # Agency_rent = tb_Agency_rent_informationd.objects.all()
    return render(request, 'Accou/rp_a_RT_agency.html',{
        # 'Agency_rent':Agency_rent,
        'Acc':Acc,
    })

########################## Report คลังถังน้ำแข็ง ###############################
def rp_a_IB_main(request):
    Acc = auth.get_user(request)
    # warehouse_information = tb_Ice_bucket_warehouse_information.objects.all()
    return render(request, 'Accou/rp_a_IB_main.html',{
        # 'warehouse_information':warehouse_information,
        'Acc':Acc,
    })

def rp_a_IB_fallow(request):
    Acc = auth.get_user(request)
    # fallow_warehouse = tb_Ice_bucket_fallow_warehouse.objects.all()
    return render(request, 'Accou/rp_a_IB_fallow.html',{
        # 'fallow_warehouse':fallow_warehouse,
        'Acc':Acc,
    })

def rp_a_IB_tracking(request):
    Acc = auth.get_user(request)
    # tracking_information = tb_Ice_bucket_tracking_information.objects.all()
    return render(request, 'Accou/rp_a_IB_tracking.html',{
        # 'tracking_information':tracking_information,
        'Acc':Acc,
    })

def rp_a_IB_lost(request):
    Acc = auth.get_user(request)
    # warehouse_lost = tb_Ice_bucket_warehouse_lost.objects.all()
    return render(request, 'Accou/rp_a_IB_lost.html',{
        # 'warehouse_lost':warehouse_lost,
        'Acc':Acc,
    })

def rp_a_IB_damaged(request):
    Acc = auth.get_user(request)
    # warehouse_damaged = tb_Ice_bucket_warehouse_damaged.objects.all()
    return render(request, 'Accou/rp_a_IB_damaged.html',{
        # 'warehouse_damaged':warehouse_damaged,
        'Acc':Acc,
    })

    #################################################################!    ADD     !################################################
# def create_budget(request):
#     form = BudgetForm()
#     if request.method == 'POST':
#         # print('Printing POST:',request.POST)
#         form = BudgetForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('appAccounting:mg_budget')

#     context = {'form': form}
#     return render(request,'Accou/form_create/create_budget.html',context)

# def update_budget(request,pk):
#     Budget_information = tb_Budget_information.objects.get(ID_budget=pk)
#     form = BudgetForm(instance=Budget_information)
#     if request.method == 'POST':
#         form = BudgetForm(request.POST, instance=Budget_information)
#         if form.is_valid():
#             form.save()
#             return redirect('appAccounting:mg_budget')
    
#     context = {'form': form}
#     return render(request,'Accou/form_create/create_budget.html',context)


# def delete_budget(request,pk):
#     Budget_information = tb_Budget_information.objects.get(ID_budget=pk)
#     if request.method == 'POST':
#         Budget_information.delete()
#         return redirect('appAccounting:mg_budget')

    
#     context ={'items': Budget_information}
#     return render(request,'Accou/form_delete/delete_budget.html',context)