from django.shortcuts import render,redirect
from django.views.generic import *
from owner.models import service_detail,s_center,service_record,payment_detail
from home.models import register
from .models import *
from django.db.models import Q
from .form import order_form
from owner .form import paymentform
from datetime import datetime

# Create your views here.
def customer(request,id):
    serviceobj=service_detail.objects.filter(s_center_obj=id)
    return render(request,'customer.html',{'service':serviceobj,'id':id})

class cusmoter(ListView):
    model = service_detail
    context_object_name = 'service'
    template_name='customer.html'

class center(ListView):
    model = s_center
    context_object_name = 'service'
    template_name='servicecenter.html'


def addtocart(request):
    if request.method=="POST":
        serviceid=request.POST['serviceid']
        sessionvalue=request.session['user']
        customerobj=register.objects.get(email=sessionvalue)
        serviceobj=service_detail.objects.get(pk=serviceid)
        service=service_detail.objects.filter(pk=serviceid)
        cartobj= cart(customerobj=customerobj,serviceobj=serviceobj,totalprice=serviceobj.price)
        cartobj.save()
        print("cartadded")
        msg= "Item Add Successfully..!!"
        return render(request,'customer.html',{'msg':msg,'service':service})
    else:
        print("cart cant create")
        return render(request,'customer.html',{'service':service})
    
def viewcard(request):
   sessionvalue=request.session['user']
   customerobject=register.objects.get(email=sessionvalue)
   cartobj=cart.objects.filter(customerobj=customerobject)
   totalamount=0
   a=0
   for i in cartobj:
        totalamount=totalamount+i.totalprice
        a=a+1
   return render(request,'viewcart.html',{'customerobj':customerobject,'cartobj':cartobj,'price':totalamount,'numberofproduct':a})

def delete_cart(request):
    if request.method == "POST":
        id=request.POST['deletecart']
        print(id)
        cartobj = cart.objects.get(id=id) 
        print(cartobj) 
        cartobj.delete()
        return redirect("../customer/viewcart")
    else:
        return render(request,'viewcart.html')

from django.contrib.auth import logout    
def logout_view(request):
    logout(request)
    return redirect("/")

def search_car(request):
    service_id=request.POST['service_id']
    sessionvalue=request.session['user']
    centerid=register.objects.get(email=sessionvalue)
    if request.method=="POST":
        service=service_detail.objects.all()
        car_name=request.POST['car_name']
        record=service_detail.objects.filter(Q(car_name__icontains=car_name) & Q(s_center_obj=service_id))
       
        return render(request,'customer.html',{'service':record,'id':service_id})
    else:
        print("not found")
        return render(request,'customer..html')
    
def search(request):
    if request.method=="POST":
        service=s_center.objects.all()
        state=request.POST['state']
        city=request.POST['city']

        if state !=" " and city != " ": 
            record=s_center.objects.filter(Q(state=state) & Q(city=city))
            return render(request,'servicecenter.html',{'service':record})
        elif state !=" " and city==" ":
            record=s_center.objects.filter(Q(state=state))
            return render(request,'servicecenter.html',{'service':record})
        elif state ==" " and city!=" ":
            record=s_center.objects.filter(Q(city=city))
            return render(request,'servicecenter.html',{'service':record})
        elif state==" " and city==" ":
            return render(request,'servicecenter.html',{'service':service})
    
    else:
        print("not found")
        return render(request,'customer..html')
    
def back(request):
    if request.method=="POST":
        return redirect("/customer/service")
    
def appintment(request):
   sessionvalue=request.session['user']
   customerobject=register.objects.get(email=sessionvalue)
   cartobj=cart.objects.filter(customerobj=customerobject)
   msg="Appoitment request send successfully Conformation maile is send to to your registerd mail address"

   totalamount=0
   service_category=""
   center_name=""
   center_email=""
   service_contact=""
   service_package_name=""
   car_name=""
   a=0

   if request.method=="POST":
       form=order_form(request.POST)
       form.instance.customer_email=sessionvalue
       form.instance.appointment_no=datetime.now().strftime("%p%Y%m%d%H%M%f")
       servicemail=request.POST['center_email']
       carname=request.POST['car_name']
       form.instance.service_center_email=servicemail
       form.instance.car_name=carname
       print(form)
       form.save()
       custobj=register.objects.get(email=sessionvalue)
       cartobj=cart.objects.filter(customerobj=custobj.id)
       cartobj.delete()
       return render(request,'order.html',{'msg':msg})

       print("success")
    
   for i in cartobj:
        totalamount=totalamount+i.totalprice
        service_category=service_category+"  "+i.serviceobj.service_category
        center_name=i.serviceobj.s_center_obj.center_name
        car_name=i.serviceobj.car_name
        center_email=i.serviceobj.s_center_obj.email
        service_contact=i.serviceobj.s_center_obj.center_phone
        service_package_name=service_package_name+"  "+i.serviceobj.service_Package_name
        
        a=a+1
   return render(request,'order.html',{'customerobj':customerobject,'cartobj':cartobj,'price':totalamount,'numberofproduct':a,'service_category':service_category,'center_name':center_name,'service_contact':service_contact,'service_package_name':service_package_name,'center_email':center_email,'car_name':car_name})

def cust_appointmentview(request):
      sessionvalue=request.session['user']
      appointmentobj=order.objects.filter(customer_email=sessionvalue)
      print(appointmentobj)
      return render(request,'cust_appointment.html',{'appintment':appointmentobj})


def go_tO_checkout(request):
     sessionvalue=request.session['user']
     if request.method=="POST":
        return redirect("../customer/appintment")
     return render(request,'viewcart.html')

def cust_profile(request):
      sessionvalue=request.session['user']
      ownerobj=register.objects.get(email=sessionvalue) 
       

      if request.method =="POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email1 = request.POST.get('email')
        phone = request.POST.get('phone')
     
        center_record=register.objects.get(email=email1)
        center_record.fname=fname
        center_record.lname=lname
        center_record.email=email1
        center_record.phone=phone
        center_record.save()

        return redirect("/customer/service")
        # return render(request,'user.html')
      else:
            return render(request,'customer_profile.html',{'user':ownerobj})
      
def view_detail(request,id):
    aptobj=order.objects.get(id=id)
    service_recordobj=service_record.objects.get(appointment_no=aptobj.appointment_no)
    total=service_recordobj.total_amount
    apt_no=request.POST.get('apt_no')
   
    if request.method == "POST":
        orderobj=service_record.objects.get(appointment_no=apt_no)
        print(orderobj)
        orderobj.payment_status="Paid"
        orderobj.status="complete"
        orderobj.save(update_fields=['payment_status'])
        orderobj.save(update_fields=['status'])
        custobj=order.objects.get(appointment_no=apt_no)
        custobj.status="complete"
        custobj.save(update_fields=['status'])
        return redirect("/customer/cust_appointmentview")
    return render(request,'appointment_detail.html',{'i':service_recordobj,'total':total})
 
def recipt(request,id):
    aptobj=order.objects.get(id=id)
    service_recordobj=service_record.objects.get(appointment_no=aptobj.appointment_no)
    total=service_recordobj.total_amount
    return render(request,'recept.html',{'i':service_recordobj,'total':total})

def gen_recept(request):
    print("In receipt")
    sessionvalue=request.session['user']
    apt_no=request.POST.get('apt_no')
    tsid=request.POST.get('tsid')
    t_amt=request.POST.get('amountpaid')
    trans_status=request.POST.get('status')
    orderobj=service_record.objects.get(appointment_no=apt_no)
    serobj=order.objects.get(appointment_no=apt_no)
    print("Before")
    if request.method == "POST":
        print("In if")
        modelboj=payment_detail(transection_id=tsid,payment_status=trans_status,amount=t_amt,appointment_no=apt_no)
        print(modelboj)
        modelboj.save()
        orderobj.payment_status="Paid"
        orderobj.status="complete"
        orderobj.save(update_fields=['payment_status'])
        orderobj.save()
        orderobj.save(update_fields=['status'])
        serobj.status="complete"
        serobj.save(update_fields=['status'])
        return redirect("/customer/cust_appointmentview")
    return render(request,'appointment_detail.html')









