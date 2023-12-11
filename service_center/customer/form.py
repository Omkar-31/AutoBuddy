from django import forms
from .models import order
from django import forms

class order_form(forms.ModelForm):
    class Meta:
        model=order
        fields=['customer_fname','customer_lname','customer_contact','service_center_name','service_center_contact','service_package',
                'service_category','Totalamount','appoinment_Date','car_no']

