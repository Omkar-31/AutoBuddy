from django.contrib import admin
from django.urls import path,include
from . import views
from home.views import *
from .views import user
from django.conf import settings
from django.conf.urls.static import static
from .views import notification
app_name='service_center'
urlpatterns = [
    path('center/',views.notification),
    path('center/',notification,name='notification'),
    path('user',views.user),
    # path('user',user.as_view()),
    path('add_service',views.add_service),
    path('profile',views.profile),
    path('car',views.car),
    path('logout',views.logout_view),
    path('delet',views.delete_record),
    path('back',views.back),
    path('viewapp',views.viewappointment),
    path('accept/<int:id>',views.accept_appointment),
    path('declined',views.reject_appointment),
    path('appointment',views.appointment),
    path('active/<int:id>',views.active_record),
    path('active_list',views.active_list),
    path('payment/<int:id>',views.payment),
    path('center_back',views.center_back),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                    document_root=settings.MEDIA_ROOT)