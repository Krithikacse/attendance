"""amss URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from .import views

urlpatterns = [
    path('',views.Home,name="Home"),
    path('studentlogin',views.studentlogin,name="studentlogin"),
    path('studentregister',views.studentregister,name="studentregister"),
    path('studentvalidate',views.studentvalidate,name="studentvalidate"),
    path('stafflogin',views.stafflogin,name="stafflogin"),
    path('get_staffs',views.get_staffs,name="get_staffs"),
    path('staffregister',views.staffregister,name="staffregister"),
    path('adminlogin',views.adminlogin,name="adminlogin"),
    path('adminregister',views.adminregister,name="adminregister"),
    path('attendancesubmit',views.attendancesubmit,name="attendancesubmit"),
    path('password_reset', auth_views.PasswordResetView.as_view(),name="reset_password"),
    path('password_reset_sent/', auth_views.PasswordResetDoneView.as_view(),name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(),name="password_reset_complete"),
    path('mail',views.mail,name="mail"),

]




    
    
