from django.shortcuts import render
from django.http import HttpResponse
from . models import *




# Create your views here.
def fn_home(request):
    return render(request,"home.html")

def fn_viewtower(request):
    return render(request,"viewtower.html")    

def fn_login(request):
    try:
        if request.method == 'POST':
            username   = request.POST['username']
            password   = request.POST['password']
            login_obj  = Login.objects.get(username=username)
            request.session['user_id']=login_obj.id
            
            if login_obj.password == password:
                if login_obj.role == 'admin':
                    return render(request,"menu.html")
                return render(request,"userhome.html")
            return HttpResponse('incorrect password')
        return render(request,"login.html")
    except Exception as e:
        print(e)
        return HttpResponse('incorrect username')
            
        
   

def fn_register(request):
    if request.method == 'POST':
        try:
            name    = request.POST['name']
            email = request.POST['email']
            mobile   = request.POST['mobile']
            username    = request.POST['username']
            password = request.POST['password']
            cpassword = request.POST['cpassword']
            
            check_exist= Login.objects.filter(username=username).exists()
            if check_exist == False:
                login_obj = Login(username=username,password=password)
                print(login_obj)
                login_obj.save()
                if login_obj.id>0:
                    register_obj=Register(name=name,mobile=mobile,cpassword=cpassword,
                    email=email,fk_login=login_obj)
                    print(register_obj)
                    register_obj.save()
                    if register_obj.id>0:
                        return HttpResponse('Registered successfully')
                return HttpResponse('success')
            return HttpResponse('already exist')
            
        except Exception as e: 
            print(e)

            return HttpResponse('invalid') 
    return render(request,"register.html")



def fn_menu(request):
    return render(request,"menu.html")

def fn_showtower(req):
    return render(req,"showtower.html")

def fn_addtower(request):
    try:
        if request.method =="POST":
            towerid       = request.session['user_id']
            towername     = request.POST['towername']
            towerlocation = request.POST['towerlocation']
            qrcode        = request.POST['qrcode']
            tower_obj     = Addtower(tower_name=towername,tower_location=towerlocation,qrcode=qrcode)
            tower_obj.save()
            print(tower_obj)
        return render(request,"addtower.html",{'towerdata':tower_obj})
    except Exception as e:
        print(e)
    
