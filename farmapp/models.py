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



