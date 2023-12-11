from django.shortcuts import render,redirect
from django.views.generic import *
from django.urls import reverse_lazy,reverse
from .models import *
from django.db.models import Q
from django.contrib.auth.hashers import make_password ,check_password

# Create your views here.
def singup(request):
        if request.method =="POST":
            fn = request.POST.get('fname')
            ln = request.POST.get('lname')
            email1 = request.POST.get('email')
            password = request.POST.get('password')
            password = make_password(password)
            phoneno = request.POST.get('phone')
            user=request.POST.get('user')
            errormsg=False
            
            cust1=register(fname=fn,lname=ln,email=email1,password=password,phone=phoneno,user_type=user)
            cust =register.objects.filter(email = email1) 

            if register.objects.filter(email = email1) :
                errormsg ="Email Already Exist"
                return render(request,'registration.html',{'errormsg': errormsg})
            else:
                cust1.save()
                return redirect('..')

            if(len(fn)<3)&(len(ln)<3):
                errormsg = "Name cannot be less than 3 charaters"
                return render(request,'registration.html',{'errormsg': errormsg})


        
            
        else:
            print("error datat else")
            return render(request,'registration.html')


def login(request):
        try:
            sessionvalue=request.session['user']
            if sessionvalue:
                userobj=register.objects.get(email=sessionvalue)
                if userobj.user_type=="Service Center" :
                    return redirect('/service_center/user')
                else:
                    return redirect('/customer/service')
        
                
        except:         
            errormsg = False
            if request.method =="POST":
                user = request.POST['user']
                password = request.POST['pass']

                try:
                    customerobj = register.objects.get(email=user)
                    print(customerobj)
                    flag = False
                
                    if customerobj:
                            flag = check_password(password,customerobj.password)
                            print(flag)
                            if flag and customerobj.user_type=="Service Center" :
                                request.session.modified = True
                                request.session['user'] = user
                                sessionvalue=request.session['user']
                                return redirect('/service_center/user')
                                
                            
                            elif flag and customerobj.user_type=="Customer" :
                                request.session.modified = True
                                request.session['user'] = user
                                return redirect('/customer/service')
                            
                    
                            else: 
                                errormsg="Invalid Username"
                                return render(request,'Home.html',{'errormsg':errormsg})
                except:                    
                    
                        errormsg="User Does Not Exist"
                        return render(request,'Home.html',{'errormsg':errormsg})
                    
            else : 
                errormsg = False
                return render(request,'Home.html',{'errormsg':errormsg})

