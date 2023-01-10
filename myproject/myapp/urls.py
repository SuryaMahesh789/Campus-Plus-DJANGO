

from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [
path('',views.home),
path('home',views.home),
path('contact',views.contact),
path('register',views.register),
path('about',views.about),
path('login',views.login),


path('registeradmin',views.registeradmin),
path('checkadmin',views.checkadmin),


path('addpage',views.addpage),
path('searchpage',views.searchpage),
path('removepage',views.removepage),
path('displaypage',views.displaypage),
path('showpage',views.showpage),

path('index',views.index),
path('addstudent',views.addstudent),
path('deladmin',views.deladmin),
path('removeadmin',views.removeadmin),
path('removestudent',views.removestudent),
path('searchstudent',views.searchstudent),


path('manage',views.manage),
path('managestudent',views.managestudent),

path('coursedetails',views.coursedetails),
]
