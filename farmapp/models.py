from django.db import models

# Create your models here.
class Login(models.Model):
    username = models.CharField(max_length=250)
    password = models.CharField(max_length=250)
    role     = models.CharField(max_length=25)
class Register(models.Model):
    name = models.CharField(max_length=250)
    email= models.CharField(max_length=250)
    mobile= models.CharField(max_length=250)
    cpassword = models.CharField(max_length=250)
    fk_login =models.ForeignKey(Login,on_delete=models.CASCADE)
    
class Rack(models.Model):
    rack_name = models.CharField(max_length=250)
    qrcode = models.CharField(max_length=250)
    
class Bay(models.Model): 
    bay_name = models.CharField(max_length=250) 
    qrcode   = models.CharField(max_length=250) 
    fk_rackid  = models.ForeignKey(Rack,on_delete=models.CASCADE)
    
class Vender(models.Model):
    vender_name= models.CharField(max_length=250)

class Tower(models.Model):
    Rack_id      = models.ForeignKey(Rack,on_delete=models.CASCADE)
    Bay_id        = models.ForeignKey(Bay,on_delete=models.CASCADE)
    tower_name     = models.CharField(max_length=250)
    tower_location = models.CharField(max_length=250)
    qrcode         = models.CharField(max_length=250)
    tower_color     = models.CharField(max_length=250)
    tower_height    = models.CharField(max_length=250)
    vender_id       =  models.ForeignKey(Vender,on_delete=models.CASCADE)


