from django.contrib import admin
from django.urls import path,include
from . import views
from home.views import *
from .views import center,cusmoter
from django.conf import settings
from django.conf.urls.static import static

app_name="customer"
urlpatterns = [
    path('cust',cusmoter.as_view(),name='customer'),
    path('customer/<int:id>',views.customer,name='customer'),
    path('service',center.as_view()),
    path('addtocart',views.addtocart),
    path('viewcart',views.viewcard),
    path('deletecart',views.delete_cart),
    path('logout',views.logout_view),
    path('search',views.search),
    path('customer/search_car',views.search_car),
    path('back',views.back),
    path('appintment',views.appintment),
    path('cust_appointmentview',views.cust_appointmentview),
    path('go_tO_checkout',views.go_tO_checkout),
    path('cust_profile',views.cust_profile),
    path('view_detail/<int:id>',views.view_detail),
    path('recipt/<int:id>',views.recipt),
    path('gen_recp',views.gen_recept),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)