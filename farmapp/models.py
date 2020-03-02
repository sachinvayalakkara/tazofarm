from django.db import models

# Create your models here.
class Login(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    role     = models.CharField(max_length=25)
class Register(models.Model):
    name = models.CharField(max_length=25)
    email= models.CharField(max_length=50)
    mobile= models.CharField(max_length=25)
    cpassword = models.CharField(max_length=25)
    fk_login =models.ForeignKey(Login,on_delete=models.CASCADE)
    

class Bay(models.Model): 
    bay_name = models.CharField(max_length=25) 
    qrcode   = models.CharField(max_length=25) 

class Rack(models.Model):
    rack_name = models.CharField(max_length=25)
    qrcode = models.CharField(max_length=25)
    fk_bayid  = models.ForeignKey(Bay,on_delete=models.CASCADE)
        
    
class Vendor(models.Model):
    vendor_name= models.CharField(max_length=25)

class Tower(models.Model):
    Rack_id      = models.ForeignKey(Rack,on_delete=models.CASCADE)
    Bay_id        = models.ForeignKey(Bay,on_delete=models.CASCADE)
    tower_name     = models.CharField(max_length=25)
    tower_location = models.CharField(max_length=25)
    qrcode         = models.CharField(max_length=25)
    tower_color     = models.CharField(max_length=25)
    tower_height    = models.CharField(max_length=25)
    vendor_id       =  models.ForeignKey(Vendor,on_delete=models.CASCADE)

class Unitmaster(models.Model):
    unit_name = models.CharField(max_length=50)

class Stages(models.Model):
    stages    = models.CharField(max_length=50)
    colorcode = models.CharField(max_length=50)
class Packingtype(models.Model):
    packing_type= models.CharField(max_length=50)

class Croptype(models.Model):
    crop_type= models.CharField(max_length=50)

class Season(models.Model):
    season= models.CharField(max_length=50)

class Crop(models.Model): 
    # id           = models.AutoField(primary_key=True, min_value=10000) 
    crop_name     = models.CharField(max_length=25) 
    crop_variety = models.CharField(max_length=25) 
    crop_desc    = models.CharField(max_length=25) 
    crop_type_id = models.ForeignKey(Croptype,on_delete=models.CASCADE) 
    unit_id            =   models.ForeignKey(Unitmaster,on_delete=models.CASCADE) 
    packing_type_id    =  models.ForeignKey(Packingtype,on_delete=models.CASCADE) 
    unit_per_pack     =  models.CharField(max_length=25) 
    season_id    =   models.ForeignKey(Season,on_delete=models.CASCADE) 
    crop_duration=  models.CharField(max_length=25) 
    mid_check =  models.CharField(max_length=25) 
    no_harvest_cutting = models.CharField(max_length=25) 
    regrow_dates   = models.CharField(max_length=25) 
     
    first_harvest =  models.CharField(max_length=25) 
    second_harvest =  models.CharField(max_length=25) 
    third_harvest =  models.CharField(max_length=25) 
    fourth_harvest = models.CharField(max_length=25) 
 
    sale_price_wholesale =  models.CharField(max_length=25) 
    sale_price_farmer=  models.CharField(max_length=25) 
    sale_price_rest = models.CharField(max_length=25) 
    soil_type       = models.CharField(max_length=25) 
    plant_distance  = models.CharField(max_length=25) 
    crop_image      = models.FileField(u"initial_picture",blank=True,upload_to="cropimages/") 
    temparature      = models.CharField(max_length=25)  

    
   

