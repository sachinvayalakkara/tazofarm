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
    
class Rack(models.Model):
    rack_name = models.CharField(max_length=25)
    qrcode = models.CharField(max_length=25)
    
    
class Bay(models.Model): 
    bay_name = models.CharField(max_length=25) 
    qrcode   = models.CharField(max_length=25) 
    fk_rackid  = models.ForeignKey(Rack,on_delete=models.CASCADE)
    
class Vender(models.Model):
    vender_name= models.CharField(max_length=25)

class Tower(models.Model):
    Rack_id      = models.ForeignKey(Rack,on_delete=models.CASCADE)
    Bay_id        = models.ForeignKey(Bay,on_delete=models.CASCADE)
    tower_name     = models.CharField(max_length=25)
    tower_location = models.CharField(max_length=25)
    qrcode         = models.CharField(max_length=25)
    tower_color     = models.CharField(max_length=25)
    tower_height    = models.CharField(max_length=25)
    vender_id       =  models.ForeignKey(Vender,on_delete=models.CASCADE)

class Unitmaster(models.Model):
    unit_name = models.CharField(max_length=50)

class Stages(models.Model):
    stages= models.CharField(max_length=50)
    colorcode = models.CharField(max_length=50)

class Croptype(models.Model):
    crop_type= models.CharField(max_length=50)

class Season(models.Model):
    season= models.CharField(max_length=50)
    
   

