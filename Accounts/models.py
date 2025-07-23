from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile = models.ImageField(upload_to='images/',default='static/assets/profile1.png')
    mobile = models.CharField(max_length=15,blank=True)
    address = models.TextField(blank=True)
    city = models.CharField(max_length=100,blank=True)
    country = models.CharField(max_length=100,blank=True)
    pin_code = models.CharField(max_length=10,blank=True)

    def __str__(self):
        return self.user.username

class Vendor(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    shop_name = models.CharField(max_length=200,blank=False,null=False)
    vendor_number = models.CharField(max_length=12,blank=False,null=False)
    vendor_address = models.CharField(max_length=200,blank=False,null=False)
    
    def __str__(self):
        return self.user.username + self.shop_name