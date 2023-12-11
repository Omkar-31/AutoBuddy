from owner.models import s_center,service_detail
from customer.models import order
from .models import *
from django import forms

class s_centerForm(forms.ModelForm):
    class Meta:
        model=s_center
        fields=['name','phone','email','state','city','center_name','center_addr','center_phone']

class serviceForm(forms.ModelForm):
    class Meta:
        model=service_detail
        fields=['car_name','service_category','price','description','service_image','service_Package_name']

class accept_appointment_form(forms.ModelForm):
    class Meta:
        model=order
        fields=['customer_fname','customer_lname','customer_email','customer_contact','service_center_name','service_center_contact','service_center_email','service_package','service_category','Totalamount','appoinment_Date','appointment_no','car_name','car_no']

class active_record_form(forms.ModelForm):
    class Meta:
        model=service_record
        fields=['customer_lname','customer_fname','appointment_no','appintment_date','car_name','car_no','customer_contact','service_category','service_package','package_amount']

class paymentform(forms.ModelForm):
    class Meta:
        model=service_record
        fields=['appointment_no','appintment_date','car_name','car_no','customer_fname','customer_lname','customer_contact','service_category','service_package','package_amount','additional_work','additional_cahrge','total_amount','delivery_date','payment_status']
