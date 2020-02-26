from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import *
from django.http import JsonResponse
from django.core import serializers




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



# def fn_menu(request):
#     return render(request,"menu.html")


def fn_menu(req):
    try:
        rack_obj = Rack.objects.all()
        bay_obj = Bay.objects.all()
        vendor_obj = Vender.objects.all()
        tower_obj = Tower.objects.all()
        return render(req,"menu.html",{'rackdata':rack_obj,'baydata':bay_obj,'vendordata':vendor_obj,'towerdata':tower_obj})
    except Exception as e:
        print(e)   


def fn_showrack(req):
    try:
        rack_obj = Rack.objects.all()               
        return render(req,"showrack.html",{'rackdata':rack_obj})      
    except Exception as e:
        print(e)           


    
    

def fn_addrack(req):
    try:
        rackname = req.POST['rackname']
        qrcode   = req.POST['qrcode']
            
        rack_obj = Rack(rack_name=rackname,qrcode=qrcode)
        rack_obj.save()  
        if rack_obj.id > 0:
            return redirect('/farmapp/showrack/')      
    except Exception as e:
        print(e)
        return render(req,"showrack.html",{'msg':'insertion failed'})




def fn_addbay(request): 
   
    try: 
        
        rack_obj = Rack.objects.all()
        # print(rack_obj)
         
        
        if request.method == "POST":
            rakid = request.POST['rackid']
            # print(rakid)
            rackname_obj    = Rack.objects.get(id=request.POST['rackid'])
            # print(rackname_obj.rack_name)
            # r_name =rackname_obj.rack_name
            bay_name     = request.POST['bayname'] 
            qrcode       = request.POST['qrcode'] 
         
            bay_obj      = Bay(bay_name=bay_name,qrcode=qrcode,fk_rackid=rackname_obj) 
            bay_obj.save() 
          
            if bay_obj.id > 0:
                return redirect('/farmapp/showbay/')   
                   
        return render(request,'showbay.html',{'rackdata':rack_obj})
        return render(request,"showbay.html") 
        
    except Exception as e: 
        print(e)
        return render(request,"showbay.html",{'msg':'insertion failed' })

def fn_showbay(request):
    try:
        bay_obj = Bay.objects.all()
        # print(bay_obj)
        return render(request,"showbay.html",{'baydata':bay_obj})
    except Exception as e:
        print(e)  

def fn_addvendor(request):
    try:
        if request.method == "POST":
           vendorname   = request.POST['vendername']
           vendor_obj   = Vender(vender_name = vendername)
           vendor_obj.save()
           if vendor_obj.id > 0:
                return redirect('/farmapp/showvendor/')
        
    except Exception as e: 
        print(e)
        return render(request,"showvendor.html",{'msg':'insertion failed' })

def fn_showvendor(req):
    try:
        vendor_obj = Vender.objects.all()
        
        return render(req,"showvendor.html",{'vendordata':vendor_obj})

    except Exception as e:
        print(e)  

def fn_addtower(request):
    try:
        rack_obj  = Rack.objects.all()
        bay_obj   = Bay.objects.filter(fk_rackid=1)
        vendor_obj= Vender.objects.all()
        
        if request.method == "POST":
            
            rackname_obj    = Rack.objects.get(id=request.POST['rackid'])
            
            bayname_obj     = Bay.objects.get(id=request.POST['bayid'])
            vendername_obj  = Vender.objects.get(id=request.POST['vendorid'])
            
            towername     = request.POST['towername']
            towerlocation = request.POST['towerlocation']
            qrcode        = request.POST['qrcode']
            towercolor    = request.POST['towercolor']
            towerheight   = request.POST['towerheight']
            tower_obj     = Tower(tower_name=towername,tower_location=towerlocation,qrcode=qrcode,tower_color= towercolor,tower_height=towerheight ,vender_id=vendername_obj,Bay_id=bayname_obj,Rack_id=rackname_obj)
            # print(tower_obj)
            tower_obj.save()

            if tower_obj.id > 0:
                return render(request,"addtower.html",{'msg':'Data entered' }) 
        return render(request,'addtower.html',{'rackdata':rack_obj,'baydata':bay_obj,'vendordata':vendor_obj})
        return render(request,"addtower.html")
    except Exception as e:
        print(e) 

def fn_showtower(req):
    try:
        tower_obj = Tower.objects.all()
        # print(tower_obj)
        return render(req,"showtower.html",{'towerdata':tower_obj})
    except Exception as e:
        print(e)  




# def fn_logout(request): 
#     # del request.session['user_id'] 
#     return render(request,'login.html')        

def fn_deleterack(req):
    try:
        service_id =req.POST['id']
        rack_obj=Rack.objects.get(id=service_id).delete()
        data ={
            'deleted':True
        }
        return JsonResponse(data)
        
             
    except Exception as e:
        print(e)

def fn_update_rack(req):
    try:
        service_id       = req.POST['id']
        print(service_id)
        rack_obj         = Rack.objects.get(id=service_id)
        # print(rack_obj.rack_name)
        # print(req.POST['rackname'])
        update=0
        if rack_obj.rack_name != req.POST['rname']:
            rack_obj .rack_name   = req.POST['rname']
            update +=1
        if rack_obj.qrcode != req.POST['qrcode']:
            rack_obj.qrcode  = req.POST['qrcode']
            update +=1
        
        if update>0:
       
            rack_obj.save()
        # rac_obj =Rack.objects.all()
        # # json_data = {rac_obj}
        # data = serializers.serialize('json',rac_obj,fields=('rack_name','qrcode') )
        return HttpResponse('update')
    except Exception as e:
        print(e)   


def fn_deletevendor(req):
    try:
        service_id =req.POST['id']
        vender_obj=Vender.objects.get(id=service_id).delete()
        data ={
            'deleted':True
        }
        return JsonResponse(data)
    except Exception as e:
        print('error')

