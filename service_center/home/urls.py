from django.contrib import admin
from django.urls import path,include
from . import views
from home.views import *

urlpatterns = [
    path('',views.login),
    path('reg',views.singup),
]