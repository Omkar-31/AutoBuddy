from django.shortcuts import render,redirect
from home import views
from home.models import register
from owner.form import s_centerForm,serviceForm,active_record_form
from owner.models import s_center,service_detail
from django.views.generic import *
from customer.models import order
from .form import accept_appointment_form,paymentform
from . models import *
from datetime import *


#Create your views here.
def user(request):
    try:
        sessionvalue=request.session['user']
        s_center_obj=s_center.objects.get(email=sessionvalue)
        service_detail_obj=service_detail.objects.filter(s_center_obj=s_center_obj.id)
        notityobj=order.objects.filter(service_center_email=sessionvalue,status="Not Approved")
        notify=0
        for i in notityobj:
            notify=notify+1

        return render(request,'user.html',{'service':service_detail_obj,'notify':notify} )
    except:
        msg="No Service Found"
        return render(request,'user.html',{'msg':msg})



def add_service(request):

    try:
        sessionvalue=request.session['user']
        serviceadd=register.objects.get(email=sessionvalue) 
        service_center_obj=s_center.objects.get(email=sessionvalue)

        if request.method =="POST":
            form=serviceForm(request.POST,request.FILES)
            form.instance.userobj = serviceadd
            form.instance.s_center_obj=service_center_obj
        
            print(form)
            form.save()
            
            return render(request,'add_service.html')
        else:
            return render(request,'add_service.html')
    except:
         msg="Please Complete Your Profile before adding service"
         return render(request,'add_service.html',{'msg':msg})


def profile(request):
      sessionvalue=request.session['user']
      ownerobj=register.objects.get(email=sessionvalue) 
       

      if request.method =="POST":
        name1 = request.POST.get('name')
        phone = request.POST.get('phone')
        email1 = request.POST.get('email')
        center_name = request.POST.get('c_name')
        state = request.POST.get('state')
        city = request.POST.get('city')
        address = request.POST.get('address')
        center_phone=request.POST.get('cphone')

        
        try:
            center_record=s_center.objects.get(email=email1)
            center_record.owner=ownerobj
            center_record.name=name1
            center_record.email=email1
            center_record.phone=phone
            center_record.state=state
            center_record.city=city
            center_record.center_addr=address
            center_record.center_name=center_name
            center_record.center_phone=center_phone
            center_record.save()
        except:
            center=s_center(owner=ownerobj,name=name1,phone=phone,email=email1,city=city,
                            state=state,center_name=center_name,
                            center_addr=address,center_phone=center_phone)
            
            center.save()
        
        # return render(request,'user.html')
        return redirect('/service_center/user')
      else:
          try:
            centerobj=s_center.objects.get(email=ownerobj.email) 
            return render(request,'profile.html',{'user':ownerobj,'center':centerobj})
          except:
            return render(request,'profile.html',{'user':ownerobj})
          

def car(request):
   return render(request,'car.html')

from django.contrib.auth import logout    
def logout_view(request):
    logout(request)
    return redirect("/")

def delete_record(request):
    if request.method == "POST":
        id=request.POST['delete_record']
        print(id)
        serviceobj = service_detail.objects.get(id=id) 
        print(serviceobj) 
        serviceobj.delete()
        return redirect("/service_center/user")
    else:
        return render(request,'user.html')
    
def back(request):
    if request.method=="POST":
        return redirect("/service_center/user")
    
def viewappointment(request):
      sessionvalue=request.session['user']
      appointmentobj=order.objects.filter(service_center_email=sessionvalue,status="Not Approved")
      print(appointmentobj)
      notityobj=order.objects.filter(service_center_email=sessionvalue,status="Not Approved")
      notify=0
      for i in notityobj:
        notify=notify+1

      return render(request,'viewappointment.html',{'appintment':appointmentobj,'notify':notify})

def accept_appointment(request,id):
    sessionvalue=request.session['user']
    appointmentobj=order.objects.get(service_center_email=sessionvalue,id=id)
    print(appointmentobj)
    form=accept_appointment_form(request.POST)
    if request.method == "POST":
        appointmentobj.status="Approved"
        appointmentobj.save(update_fields=['status'])
        return redirect("/service_center/viewapp")
    #email
    from django.core.mail import EmailMessage
    send_mail=EmailMessage('Hello','Your Appointment is sheduled for your requested date. Thank You for choosing us.' , to=[appointmentobj.customer_email])
    send_mail.send()
    print("send")
    return render(request,'accept_appointment.html',{'i':appointmentobj,'id':id})

def reject_appointment(request):
    id1=request.POST.get('id')
    print(id1)
    sessionvalue=request.session['user']
    appointmentobj=order.objects.get(service_center_email=sessionvalue,id=id1)
    print(appointmentobj)
    form=accept_appointment_form(request.POST)
    if request.method == "POST":
        appointmentobj.status="Declined"
        appointmentobj.save(update_fields=['status'])
        return redirect("/service_center/viewapp")
    from django.core.mail import EmailMessage
    send_mail=EmailMessage('Hello','Soory for the inconvenince we are unable to shedual your appointment for respective date due to sevral issues you can place order again for another date Thank You.' , to=['omkarm904@gmail.com'])
    send_mail.send()
    print("send")
    return render(request,'accept_appointment.html',{'i':appointmentobj})

def appointment(request):
      sessionvalue=request.session['user']
      appointmentobj=order.objects.filter(service_center_email=sessionvalue,status="Approved")
      notityobj=order.objects.filter(service_center_email=sessionvalue,status="Not Approved")
      notify=0
      for i in notityobj:
        notify=notify+1
      print(appointmentobj)
      return render(request,'approved_list.html',{'appintment':appointmentobj,'notify':notify})


def active_record(request,id):
    sessionvalue=request.session['user']
    appointmentobj=order.objects.get(service_center_email=sessionvalue,id=id)
    print(appointmentobj)
    form=accept_appointment_form(request.POST)
    form1=active_record_form(request.POST)
    appointment_no=request.POST.get('appointment_no')
    appintment_date=request.POST.get('appintment_date')
    customer_fname=request.POST.get('customer_fname')
    customer_lname=request.POST.get('customer_lname')
    customer_contact=request.POST.get('customer_contact')
    service_category=request.POST.get('service_category')
    service_package=request.POST.get('service_package')
    package_amount=request.POST.get('package_amount')
    car_name=request.POST.get('car_name')
    car_no=request.POST.get('car_no')
    date=datetime.now().strftime("%Y-%m-%d")
    print(date)
    if request.method == "POST":
        appointmentobj.status="Active"
        appointmentobj.save(update_fields=['status'])
        obj=service_record(appointment_no=appointment_no,email=sessionvalue,appintment_date=date,customer_fname=customer_fname,customer_lname=customer_lname,customer_contact=customer_contact,service_category=service_category,service_package=service_package,package_amount=package_amount,car_name=car_name,car_no=car_no)
        obj.save()
        return redirect("/service_center/appointment")
    return render(request,'active_record.html',{'i':appointmentobj})

def approved_record(request,id):
    sessionvalue=request.session['user']
    appointmentobj=order.objects.get(service_center_email=sessionvalue,id=id)
    print(appointmentobj)
    form=accept_appointment_form(request.POST)
    if request.method == "POST":
        appointmentobj.status="Approved"
        appointmentobj.save(update_fields=['status'])
        return redirect("/service_center/viewapp")
    return render(request,'active_record.html',{'i':appointmentobj})

def active_list(request):
    sessionvalue=request.session['user']
    print(sessionvalue)
    activeobj=service_record.objects.filter(email=sessionvalue)
    notityobj=order.objects.filter(service_center_email=sessionvalue,status="Not Approved")
    notify=0
    for i in notityobj:
        notify=notify+1
    
    return render(request,'active_list.html',{'activeobj':activeobj,'notify':notify})  

def payment(request,id):
    sessionvalue=request.session['user']
    form=paymentform(request.POST)
    appointmentobj=service_record.objects.get(email=sessionvalue,id=id)
    appointment_no1=request.POST.get('appointment_no')
    appintment_date=request.POST.get('appintment_date')
    car_name=request.POST.get('car_name')
    car_no=request.POST.get('car_no')
    customer_fname=request.POST.get('customer_fname')
    customer_lname=request.POST.get('customer_lname')
    customer_contact=request.POST.get('customer_contact')
    service_category=request.POST.get('service_category')
    service_package=request.POST.get('service_package')
    package_amount=request.POST.get('package_amount')

    additional_work=request.POST.get('additional_work')
    additional_cahrge=request.POST.get('additional_cahrge')
    total_amount=request.POST.get('total_amount')
    delivery_date=request.POST.get('delivery_date')
    payment_status=request.POST.get('payment_status')
    payment_mode=request.POST.get('payment_mode')


    if request.method=="POST":
        recordobj=service_record.objects.get(appointment_no=appointment_no1)
        recordobj.appintment_date=appintment_date
        recordobj.car_name=car_name
        recordobj.car_no=car_no
        recordobj.customer_fname=customer_fname
        recordobj.customer_lname=customer_lname
        recordobj.customer_contact=customer_contact
        recordobj.service_category=service_category
        recordobj.service_package=service_package
        recordobj.package_amount=package_amount
        recordobj.additional_work=additional_work
        recordobj.additional_cahrge=additional_cahrge
        recordobj.total_amount=total_amount
        recordobj.delivery_date=delivery_date
        recordobj.payment_status=payment_status
        recordobj.payment_mode=payment_mode
        recordobj.save()

        cust_record_obj=order.objects.get(service_center_email=sessionvalue,appointment_no=appointment_no1)
        if payment_status=="Paid" :
            recordobj.status="complete"
            cust_record_obj.status="complete"
            recordobj.save()
            cust_record_obj.save()
        if recordobj.status=="complete":
            recordobj.payment_status="Paid"
            recordobj.save()
        return redirect("/service_center/active_list")
    return render(request,'payment.html',{'i':appointmentobj})

from django.http import JsonResponse
def notification(request):
    sessionvalue=request.session['user']
    notityobj=order.objects.filter(service_center_email=sessionvalue)
    print(notityobj)
    notify=0
    for i in notityobj:
        notify=notify+1
    print(notify)
    return render(request,'header.html',{'notify':notify})
        
def center_back(request):
    if request.method=="POST":
        return redirect("/service_center/user")

    


    
