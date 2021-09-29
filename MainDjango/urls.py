"""end1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse

urlpatterns = [
    # path('jet/', include('jet.urls', 'jet')),  # Django JET URLSjango JET URLS
    # path(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    path('admin/', admin.site.urls, name="admin"),
    # path('admin/logout/', 'appMain.views.form_login'),
    path('',include(('appMain.urls','appMain'),namespace='appMain')),
    path('form_login/',include(('appMain.urls','appMain'),namespace='appMain')),
    # path('login/',include(('appMain.urls','appMain'),namespace='appMain')),
    path('check_login/',include(('appMain.urls','appMain'),namespace='appMain')),
    path('Ceo_index/',include(('appCeo.urls','appCeo'),namespace='appCeo')),
    path('Accounting_index/',include(('appAccounting.urls','appAccounting'),namespace='appAccounting')),
    path('Sales_index/',include(('appSales.urls','appSales'),namespace='appSales')),



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
