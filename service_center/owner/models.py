from django.db import models
from home.models import register


# Create your models here.
class s_center(models.Model):

    owner=models.ForeignKey(register,on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    email=models.EmailField()
    phone=models.BigIntegerField()
    state=models.CharField(max_length=255)
    city=models.CharField(max_length=255)
    center_name=models.CharField(max_length=255)
    center_addr=models.CharField(max_length=255)
    center_phone=models.BigIntegerField()

    class Meta:
        db_table="service_center"




class service_detail(models.Model):
    car_name = (("Bolero","Bolero"),("BR-V","BR-V"),("scorpio","scorpio"),("XUV500","XUV500"),("Aspire","Aspire"))
    service = (("Periodic services","Periodic services"),("AC Service","AC Service"),("Denting and Penting","Denting and Penting"),("Car Batteries","Car Batteries"),("Tayers and Wheel Care","Tayers and Wheel Care"),("Car Spa","Car Spa"))
    s_center_obj=models.ForeignKey(s_center,on_delete=models.CASCADE)
    userobj=models.ForeignKey(register,on_delete=models.CASCADE)
    service_image=models.ImageField(upload_to="media")
    service_Package_name=models.CharField(max_length=350,null=True)
    car_name=models.CharField(max_length=255,choices=car_name)
    service_category=models.CharField(max_length=255,choices=service)
    price=models.IntegerField()
    description=models.CharField(max_length=350)
    class Meta:
        db_table="service_Detail"

class service_record(models.Model):
    email=models.EmailField(default=None,blank=True,null=True)
    appointment_no=models.CharField(max_length=255)
    appintment_date=models.CharField(max_length=500)
    car_name=models.CharField(max_length=255)
    car_no=models.CharField(max_length=255)
    customer_fname=models.CharField(max_length=255)
    customer_lname=models.CharField(max_length=255)
    customer_contact=models.BigIntegerField()
    service_category=models.CharField(max_length=255)
    service_package=models.CharField(max_length=255)
    package_amount=models.FloatField()
    additional_work=models.CharField(max_length=255,default="")
    additional_cahrge=models.FloatField(default=0)
    total_amount=models.FloatField(default=0)
    delivery_date=models.CharField(max_length=255,null=True,default="Not Deliverd",blank=True)
    payment_mode=models.CharField(max_length=255,default="online")
    payment_status=models.CharField(max_length=255,default="Pending")
    status=models.CharField(max_length=255,default="Active")

    class Meta:
        db_table="service_record_detail"


class service_record_detail(models.Model):
    appointment_no=models.CharField(max_length=255)
    appintment_date=models.DateField()
    car_name=models.CharField(max_length=255)
    car_no=models.CharField(max_length=255)
    customer_fname=models.CharField(max_length=255)
    customer_lname=models.CharField(max_length=255)
    customer_contact=models.BigIntegerField()
    service_category=models.CharField(max_length=255)
    service_package=models.CharField(max_length=255)
    package_amount=models.FloatField()
    additional_work=models.CharField(max_length=255,default="")
    additional_cahrge=models.FloatField(default=0)
    total_amount=models.FloatField(default=0)
    delivery_date=models.DateField(null=True,default=None,blank=True)
    payment_status=models.CharField(max_length=255,default="Pending")
    status=models.CharField(max_length=255,default="Active")

    class Meta:
        db_table="service_center_record_detail"
class payment_detail(models.Model):
    transection_id=models.CharField(max_length=300)
    payment_status=models.CharField(max_length=300)
    amount=models.CharField(max_length=300)
    appointment_no=models.CharField(max_length=300)

    class Meta:
        db_table="payment_detail"


