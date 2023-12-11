from django.db import models
from owner.models import service_detail
from home.models import register

# Create your models here.
class cart(models.Model):
    customerobj = models.ForeignKey(register,on_delete=models.CASCADE)
    serviceobj = models.ForeignKey(service_detail,on_delete=models.CASCADE)
    totalprice = models.FloatField()
    
    class Meta:
        db_table = 'cart'

class order(models.Model):
    customer_fname=models.TextField(max_length=255)
    customer_lname=models.TextField(max_length=255)
    customer_email=models.EmailField()
    customer_contact=models.TextField(max_length=255)
    service_center_name=models.TextField(max_length=255)
    service_center_contact=models.TextField(max_length=255)
    service_center_email=models.EmailField(default="")
    service_package=models.TextField(max_length=255)
    service_category=models.TextField(max_length=255)
    Totalamount=models.FloatField()
    appoinment_Date=models.DateField()
    status=models.CharField(max_length=255,default="Not Approved")
    appointment_no=models.CharField(max_length=255,default=0)
    car_name=models.CharField(max_length=255,default="")
    car_no=models.CharField(max_length=255,default=0)

    class Meta:
        db_table='Appointment'
