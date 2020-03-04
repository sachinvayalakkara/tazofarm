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
                
                login_obj.save()
                if login_obj.id>0:
                    register_obj=Register(name=name,mobile=mobile,cpassword=cpassword,
                    email=email,fk_login=login_obj)
                    
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
        vendor_obj = Vendor.objects.all()
        tower_obj = Tower.objects.all()
        crop_obj =Crop.objects.all()
        return render(req,"menu.html",{'rackdata':rack_obj,'baydata':bay_obj,'vendordata':vendor_obj,'towerdata':tower_obj,'cropdata':crop_obj})
    except Exception as e:
        print(e)   


def fn_showrack(req):
    try:
        rack_obj = Rack.objects.all() 
        bay_obj = Bay.objects.all()            
        return render(req,"showrack.html",{'rackdata':rack_obj,'baydata':bay_obj})      
    except Exception as e:
        print(e)           


    
    

def fn_addrack(req):
    try:
        rackname = req.POST['rackname']
        qrcode   = req.POST['qrcode']
        # rack_obj = Rack.objects.all()
        # bayid = request.POST['rackid']
        # print(bayid)
        bayname_obj    = Bay.objects.get(id=req.POST['bayid'])
        # print(bayname_obj.bay_name) 

        rack_obj = Rack(rack_name=rackname,qrcode=qrcode,fk_bayid=bayname_obj)
        rack_obj.save()  
        if rack_obj.id > 0:
            return redirect('/farmapp/showrack/')      
    except Exception as e:
        print(e)
        return render(req,"showrack.html",{'msg':'insertion failed'})

def fn_showbay(request):
     
    try:
        
        bay_obj =Bay.objects.all()
        # print(bay_obj)
        return render(request,"showbay.html",{'baydata':bay_obj})
    except Exception as e:
        print(e)  

def fn_addbay(request): 
   
    try:
       
        if request.method == "POST":
           
           
            bay_name     = request.POST['bayname'] 
            # print(bay_name)
            qrcode       = request.POST['qrcode'] 
         
            bay_obj      = Bay(bay_name=bay_name,qrcode=qrcode) 
            # print(bay_obj)
            bay_obj.save() 
            # print(bay_obj)
          
            if bay_obj.id > 0:
                return redirect('/farmapp/showbay/')
           
        return render(request,"showbay.html")   
        
   
        
    except Exception as e: 
        print(e)
        # return render(request,"showbay.html",{'msg':'insertion failed' })



def fn_addvendor(request):
    try:
        if request.method == "POST":
           vendorname   = request.POST['vendorname']
        #    print(vendorname)
           vendor_obj   = Vendor(vendor_name = vendorname)
           vendor_obj.save()
           if vendor_obj.id > 0:
                return redirect('/farmapp/showvendor/')
        # return render(request,'showvendor.html')
    except Exception as e: 
        print(e)
        return render(request,"showvendor.html",{'msg':'insertion failed' })

def fn_showvendor(req):
    try:
        vendor_obj = Vendor.objects.all()
        
        return render(req,"showvendor.html",{'vendordata':vendor_obj})

    except Exception as e:
        print(e)  

def fn_addtower(request):

    try:
       
      
        if request.method == "POST":
            
            rackname_obj    = Rack.objects.get(id=request.POST['rackid'])
            
            bayname_obj     = Bay.objects.get(id=request.POST['bayid'])
            vendorname_obj  = Vendor.objects.get(id=request.POST['vendorid'])
            
            towername     = request.POST['towername']
            towerlocation = request.POST['towerlocation']
            qrcode        = request.POST['qrcode']
            towercolor    = request.POST['towercolor']
            towerheight   = request.POST['towerheight']
            tower_obj     = Tower(tower_name=towername,tower_location=towerlocation,qrcode=qrcode,tower_color= towercolor,tower_height=towerheight ,vendor_id=vendorname_obj,Bay_id=bayname_obj,Rack_id=rackname_obj)
        
            tower_obj.save()

            if tower_obj.id > 0:
                return redirect("/farmapp/tower/") 
            return render(request,"showtower.html")
        
    except Exception as e:
        print(e) 

def fn_showtower(req):
    try:
        rack_obj  = Rack.objects.all()
        bay_obj   = Bay.objects.all()
        vendor_obj= Vendor.objects.all()
        # print(vendor_obj)
        tower_obj = Tower.objects.all()
       
        return render(req,"showtower.html",{'rackdata':rack_obj,'baydata':bay_obj,'vendordata':vendor_obj,'towerdata':tower_obj})
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

def fn_deletebay(req):
    try:
        service_id =req.POST['id']
        bay_obj=Bay.objects.get(id=service_id).delete()
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
        print(rack_obj.rack_name)
        # print(req.POST['rname'])
        update=0
        if rack_obj.rack_name != req.POST['rname']:
            rack_obj .rack_name   = req.POST['rname']
            update +=1
        if rack_obj.qrcode != req.POST['qrcode']:
            rack_obj.qrcode  = req.POST['qrcode']
            update +=1

        if rack_obj.fk_bayid.bay_name != req.POST['bname']:
            rack_obj.fk_bayid.bay_name   = req.POST['bname']
            update +=1
        
        if update>0:
       
            rack_obj.save()
        # rac_obj =Rack.objects.all()
        # # json_data = {rac_obj}
        # data = serializers.serialize('json',rac_obj,fields=('rack_name','qrcode') )
        return HttpResponse('update')
    except Exception as e:
        print(e) 


def fn_update_bay(req):
    try:
        service_id    = req.POST['id']
        print(service_id)
        bay_obj      = Bay.objects.get(id=service_id)
        print(bay_obj.bay_name)
    
        update=0
        if bay_obj.bay_name != req.POST['bname']:
            bay_obj.bay_name = req.POST['bname']
            update +=1

       

        if bay_obj.qrcode != req.POST['qrcode']:
            bay_obj.qrcode  = req.POST['qrcode']
            update +=1
        
        if update>0:
       
            bay_obj.save()
        # rac_obj =Rack.objects.all()
        # # json_data = {rac_obj}
        # data = serializers.serialize('json',rac_obj,fields=('rack_name','qrcode') )
        return HttpResponse('update')
    except Exception as e:
        print(e)     


def fn_deletevendor(req):
    try:
        service_id =req.POST['id']
        vendor_obj=Vendor.objects.get(id=service_id).delete()
        data ={
            'deleted':True
        }
        return JsonResponse(data)
    except Exception as e:
        print('error')

def fn_update_vendor(req):
    try:
        service_id       = req.POST['id']
        print(service_id)
        vendor_obj         = Vendor.objects.get(id=service_id)
        print(vendor_obj.vendor_name)
        # print(req.POST['rname'])
        update=0
        if vendor_obj.vendor_name != req.POST['vname']:
            vendor_obj.vendor_name   = req.POST['vname']
            update +=1
        
        
        if update>0:
       
            vendor_obj.save()
        # rac_obj =Rack.objects.all()
        # # json_data = {rac_obj}
        # data = serializers.serialize('json',rac_obj,fields=('rack_name','qrcode') )
        return HttpResponse('update')
    except Exception as e:
        print(e) 

def fn_deletetower(req):
    try:
        service_id =req.POST['id']
        vender_obj=Tower.objects.get(id=service_id).delete()
        data ={
            'deleted':True
        }
        return JsonResponse(data)
    except Exception as e:
        print('error')

def fn_update_tower(req):
    try:
        service_id    = req.POST['id']
        print(service_id)
        tower_obj      = Tower.objects.get(id=service_id)
        print(tower_obj.tower_name)
        # print(req.POST['rname'])
        update=0
        if tower_obj.tower_name != req.POST['tname']:
            tower_obj.tower_name = req.POST['tname']
            update +=1

        if tower_obj.tower_location  != req.POST['towerlocation']:
            tower_obj.tower_location = req.POST['towerlocation']
            update +=1

        if tower_obj.qrcode != req.POST['qrcode']:
            tower_obj.qrcode= req.POST[' qrcode']
            update +=1

        if tower_obj.tower_color!= req.POST['towercolor']:
            tower_obj.tower_color= req.POST['towercolor']
            update +=1

        if tower_obj.tower_height!= req.POST['towerheight']:
            tower_obj.tower_height= req.POST['towerheight']
            update +=1
    
        if tower_obj.Rack_id.rack_name!= req.POST['rackname']:
            tower_obj.Rack_id.rack_name= req.POST['rackname']
            update +=1

        if tower_obj.Bay_id.bay_name!= req.POST['bayname']:
            tower_obj.Bay_id.bay_name = req.POST['bayname']
            update +=1   

        if tower_obj.vendor_id.vendor_name!= req.POST['vendorname']:
            tower_obj.vendor_id.vendor_name = req.POST['vendorname']
            update +=1        
        
    
        if update>0:
       
            tower_obj.save()
        # rac_obj =Rack.objects.all()
        # # json_data = {rac_obj}
        # data = serializers.serialize('json',rac_obj,fields=('rack_name','qrcode') )
        return HttpResponse('update')
    except Exception as e:
        print(e)  



def fn_showpackingtype(request):
     
    try:
        
        pack_obj = Packingtype.objects.all()
        return render(request,"showpackingtype.html",{'packdata':pack_obj})
        
    except Exception as e:
        print(e)  

def fn_addpackingtype(request): 
   
    try:
       
        if request.method == "POST":
           
           
            packingtype     = request.POST['packingtype'] 
            # print(packingtype)
           
            pack_obj      = Packingtype(packing_type=packingtype) 
    
            pack_obj.save() 
            # print(pack_obj)
          
        if pack_obj.id > 0:

            return redirect('/farmapp/showpackingtype/')
           
            return render(request,"showpackingtype.html")
    except Exception as e: 
        print(e)
        # return render(request,"showbay.html",{'msg':'insertion failed' })

def fn_delete_packingtype(request):
    try:
        service_id =request.POST['id']
        pack_obj= Packingtype.objects.get(id=service_id).delete()
        data ={
            'deleted':True
        }
        return JsonResponse(data)
    except Exception as e:
        print('error') 


def fn_showstages(request):
     
    try:
        
        stages_obj = Stages.objects.all()
        return render(request,"showstages.html",{'stagedata':stages_obj})
    except Exception as e:
        print(e)  

def fn_addstages(request): 
   
    try:
       
        if request.method == "POST":
            stages    = request.POST['stages'] 
            print(stages)
           
            colorcode       = request.POST['color_code'] 
            print(colorcode)

         
            stages_obj      = Stages(stages=stages,colorcode=colorcode) 
            
            stages_obj.save() 
            print(stages_obj)
          
            if stages_obj.id > 0:
                return redirect('/farmapp/showstages/')
           
        return render(request,"showstages.html")   
        
   
    except Exception as e: 
        print(e)
        # return render(request,"showbay.html",{'msg':'insertion failed' })

def fn_deletestages(req):
    try:
        service_id =req.POST['id']
        stages_obj= Stages.objects.get(id=service_id).delete()
        data ={
            'deleted':True
        }
        return JsonResponse(data)
    except Exception as e:
        print('error') 



def fn_showcroptype(request):
     
    try:
        
        crop_obj = Croptype.objects.all()
        # print(crop_obj)
        
        return render(request,"showcroptype.html",{'cropdata':crop_obj})
        return render(request,"showcroptype.html")
    except Exception as e:
        print(e)  

def fn_addcroptype(request): 
   
    try:
       
        if request.method == "POST":
           
           
            croptype     = request.POST['croptype'] 
            # print(croptype)
            
         
            croptype_obj     = Croptype(crop_type= croptype) 
            
            croptype_obj.save() 
            # print(croptype_obj)
          
        if croptype_obj.id > 0:
            return redirect('/farmapp/showcroptype/')
           
        return render(request,"showcroptype.html")   
        
   
        
    except Exception as e: 
        print(e)
        # return render(request,"showbay.html",{'msg':'insertion failed' })
    
def fn_deletecroptype(req):
    try:
        service_id =req.POST['id']
        croptype = Croptype.objects.get(id=service_id).delete()
        data ={
            'deleted':True
        }
        return JsonResponse(data)
    except Exception as e:
        print('error') 

def fn_showcrop(req):
    try:
        crop_obj = Crop.objects.all()
        # print(crop_obj.crop_image) 
        croptype_obj = Croptype.objects.all()
        unit_obj     = Unitmaster.objects.all()
        # print(unit_obj)
        season_obj    = Season.objects.all()
        packingtype_obj = Packingtype.objects.all()
        # print(packingtype_obj)


        return render(req,'showcrop.html',{'cropdata':crop_obj,'croptypedata':croptype_obj,'unitdata':unit_obj,'seasondata':season_obj,'packdata':packingtype_obj})

    except Exception as e:
        print(e) 

def fn_addcrop(request):

    try:
       
      
        if request.method == "POST":
            
            Crop_Type   = Croptype.objects.get(id=request.POST['croptypeid'])
            
            Unit_id     = Unitmaster.objects.get(id=request.POST['unitid'])
            season      = Season.objects.get(id=request.POST['seasonid'])
            # print(season)
            p_id = request.POST['packingid']
            # print(p_id)
            Pack = Packingtype.objects.get(id=request.POST['packingid'])
            # print(Pack)
            cropname     = request.POST['cropname']
            # print(cropname)
            variety = request.POST['variety']
            # print(cropname)
            Description        = request.POST['cropdesc']
            # print(Description)
            Crop_Duration    = request.POST['crop_duration']
            # print(Crop_Duration)
            Midway_Checkperiod   = request.POST['midway_check']
            ReadyforHarvest     = request.POST['ready_4_harvest']
            second_harvest     = request.POST['2_harvest']
            third_harvest     = request.POST['3_harvest']
            fourth_harvest     = request.POST['4_harvest']
            no_of_harvest     = request.POST['no_harvest']
            Regrow_days         = request.POST['regrow_days']
            Unitperpack         = request.POST['unit_per_pack']
            price_Wholesale      = request.POST['sp_wholesale']
            price_farmer        = request.POST['sp_farmer']
            price_Restarunt     = request.POST['sp_rest']
            soiltype            = request.POST['soiltype']
            plant_distance     = request.POST['distance']
            Temperature     = request.POST['temp']
        
            if request.FILES:
                cropimage     = request.FILES['image']
                # print(cropimage)

            crop_obj     = Crop(crop_name=cropname,crop_variety=variety,crop_desc=Description,crop_type_id= Crop_Type,
            unit_id=Unit_id ,packing_type_id=Pack,unit_per_pack=Unitperpack,season_id=season,crop_duration=Crop_Duration,
            mid_check=Midway_Checkperiod,no_harvest_cutting=no_of_harvest,regrow_dates=Regrow_days,first_harvest=ReadyforHarvest,
            second_harvest=second_harvest,third_harvest=third_harvest,fourth_harvest=fourth_harvest,
            sale_price_wholesale=price_Wholesale,sale_price_farmer=price_farmer,sale_price_rest=price_Restarunt,soil_type=soiltype,plant_distance=plant_distance,
            temparature=Temperature,crop_image= cropimage)

        
            crop_obj.save()
            # print(crop_obj)

            if crop_obj.id > 0:
                return redirect("/farmapp/showcrop/") 
        return render(request,"showcrop.html")
        
    except Exception as e:
        print(e) 
         
      
def fn_deletecrop(req):
    try:
        service_id = req.POST['id']
        croptype = Crop.objects.get(id=service_id).delete()
        data ={
            'deleted':True
        }
        return JsonResponse(data)
    except Exception as e:
        print(e) 

def fn_editcrop(req):
    try:
        
        edit_id=req.GET['id']
        # print(edit_id)
        
        crop_edit_obj=Crop.objects.get(id=edit_id)
        pack_obj     =Packingtype.objects.all()
        season_obj   =Season.objects.all()
        unit        =Unitmaster.objects.all()
        croptyp    =Croptype.objects.all()
        # print(croptyp)
        return render(req,'editcrop.html',{'editdata':crop_edit_obj,'packdata':pack_obj,'seasondata':season_obj,'unitdata':unit,
        'croptype':croptyp})

    except Exception as e:
        print(e) 

def fn_updatecrop(req):
    try:
        service_id    = req.POST['id']
        print(service_id)
        crop_obj = Crop.objects.get(id=service_id)
      
        print(crop_obj.crop_image)
        
        # croptype= Croptype.objects.get(id=req.POST['crop_typeid'])
        # print(croptype)
    

        update=0
        if crop_obj.crop_name != req.POST['cropname']:
            crop_obj.crop_name = req.POST['cropname']
            print(crop_obj.crop_name)
            update +=1
        if crop_obj.crop_variety != req.POST['c_variety']:
            crop_obj.crop_variety = req.POST['c_variety']
            print(crop_obj.crop_variety)
            update +=1
        if crop_obj.crop_desc != req.POST['c_desc']:
            crop_obj.crop_desc = req.POST['c_desc']
            print(crop_obj.crop_desc)
            update +=1
        if crop_obj.crop_type_id.id!= req.POST['crop_typeid']:
            crop_obj.crop_type_id.id= req.POST['crop_typeid']
            print(crop_obj.crop_type_id.id)
            update +=1
        if crop_obj.packing_type_id.id != req.POST['packing_id']:
            crop_obj.packing_type_id.id= req.POST['packing_id']
            print(crop_obj.packing_type_id.id)
            update +=1
        
        if crop_obj.unit_id.id != req.POST['unit_id']:
            crop_obj.unit_id.id = req.POST['unit_id']
            print(crop_obj.unit_id.id)
            update +=1    
        
        if crop_obj.unit_per_pack != req.POST['unit_perpack']:
            crop_obj.unit_per_pack = req.POST['unit_perpack']
            print(crop_obj.unit_per_pack)
            update +=1

        if crop_obj.season_id.id != req.POST['season_id']:
            crop_obj.season_id.id = req.POST['season_id']
            print(crop_obj.season_id.id)
            update +=1

        if crop_obj.crop_duration != req.POST['c_duration']:
            crop_obj.crop_duration = req.POST['c_duration']
            print(crop_obj.crop_duration)
            update +=1

        if crop_obj.mid_check != req.POST['mid_check']:
            crop_obj.mid_check = req.POST['mid_check']
            print(crop_obj.mid_check)
            update +=1

        if crop_obj.no_harvest_cutting != req.POST['noharvest']:
            crop_obj.no_harvest_cutting = req.POST['noharvest']
            print(crop_obj.no_harvest_cutting)
            update +=1
        
        if crop_obj.regrow_dates != req.POST['regrow_days']:
            crop_obj.regrow_dates = req.POST['regrow_days']
            print(crop_obj.regrow_dates)
            update +=1    

        if crop_obj.first_harvest != req.POST['first_harvest']:
            crop_obj.first_harvest = req.POST['first_harvest']
            print(crop_obj.first_harvest)
            update +=1

        if crop_obj.second_harvest != req.POST['secondharvest']:
            crop_obj.second_harvest = req.POST['secondharvest']
            print(crop_obj.second_harvest)
            update +=1

        if crop_obj.third_harvest != req.POST['thirdharvest']:
            crop_obj.third_harvest = req.POST['thirdharvest']
            print(crop_obj.third_harvest)
            update +=1

        if crop_obj.fourth_harvest != req.POST['fourthharvest']:
            crop_obj.fourth_harvest = req.POST['fourthharvest']
            print(crop_obj.fourth_harvest)
            update +=1

        if crop_obj.sale_price_wholesale != req.POST['spwholesale']:
            crop_obj.sale_price_wholesale = req.POST['spwholesale']
            print(crop_obj.sale_price_wholesale)
            update +=1
        
        if crop_obj.sale_price_farmer != req.POST['spfarmer']:
            crop_obj.sale_price_farmer = req.POST['spfarmer']
            print(crop_obj.sale_price_farmer)
            update +=1    

        if crop_obj.sale_price_rest != req.POST['sp_rest']:
            crop_obj.sale_price_rest = req.POST['sp_rest']
            print(crop_obj.sale_price_rest)
            update +=1

        if crop_obj.soil_type != req.POST['soil_type']:
            crop_obj.soil_type = req.POST['soil_type']
            print(crop_obj.soil_type)
            update +=1

        if crop_obj.plant_distance != req.POST['distance']:
            crop_obj.plant_distance = req.POST['distance']
            print(crop_obj.plant_distance)
            update +=1
        
        if crop_obj.temparature != req.POST['temp']:
            crop_obj.temparature = req.POST['temp']
            print(crop_obj.temparature)
            update +=1

        if crop_obj.crop_image != req.POST['c_image']:
            crop_obj.crop_image = req.POST['c_image']
            print(crop_obj.crop_image)
            update +=1

        if update>0:
       
            crop_obj.save()
        return HttpResponse('update')
    except Exception as e:
        print(e) 


    

