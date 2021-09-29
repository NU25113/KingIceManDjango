from os import name
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.urls import reverse

from django.contrib.auth.models import auth,User,Group
# from appAdmin.models import tb_user
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user
from django.contrib.auth import logout
from django.shortcuts import redirect


# Create your views here.
from .forms import CreatUserForm

# from .decorators import unauthenticated_user,allowed_users,admin_only



def index(request):
    return render(request,'index.html')

def form_login(request):
    logout(request)
    # return redirect(reverse('appMain:form_login'))
    return render(request,"main/form_login.html")

# def admin(request):
#     return render(request,'main/admin_loggin.html')
def Sign_In(request):
    return render(request,"main/test_login.html")
# def test_login(request):
#     if request.method == 'POST':
#        username = request.POST["username"]
#        print(username)
#     return redirect ("appMain:test_login")
    #   return render(request,"main/test_login.html")

# @unauthenticated_user
def register (request):
    
    form = CreatUserForm()

    if request.method == 'POST':
        form = CreatUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            
            group = Group.objects.get(name='Ceo')
            user.group.add(group)

            messages.SUCCESS(request,'สร้างบัญชีสำเร็จแล้ว' + username)

            return redirect('appMain:form_login')
            # return redirect('dashboard')

    context = {'form': form}
    return render(request, "main/register.html", context)



@unauthenticated_user
def login(request):
    if request.method == 'POST':
        username =  request.POST ["username"]
        password =  request.POST ["password"]

        user =  auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect("appCeo:index")

        else:
            messages.info(request,'ชื่อผู้ใช้ หรือ รหัสผ่านไม่ถูกต้อง')
            return render(request,"main/form_login.html")

    context = {}
    return render(request,"main/form_login.html",context)


def logout(request):
    auth.logout(request)
    return redirect ("appMain:index")
# @csrf_exempt
# def check_login(request):
        # return render(request, 'main/check_login.php') 

