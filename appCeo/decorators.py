from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from functools import wraps
from django.contrib.auth.models import User,auth


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('appCeo:index')

        else:
            return view_func(request, *args, **kwargs)

        
    return wrapper_func

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper_func(request, *args, **kwargs):
            if request.user.groups.filter(name__in=allowed_roles).exists():
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('คุณไม่ได้รับอนุญาติให้ดูหน้านี้')

        return wrapper_func
    return decorator

def admin_only(view_func):
    def wrapper_function(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group == 'Ceo':
                # return redirect('appCeo:index')
                return render(request, 'ceo/index.html')
            if group == 'admin':
                return view_func(request, *args, **kwargs)
            else:
                return redirect('admin:index')
                
    return wrapper_function
    