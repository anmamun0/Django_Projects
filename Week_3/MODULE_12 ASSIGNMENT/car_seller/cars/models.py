from django.db import models
from brands.models import Brand
from django.contrib.auth.models import User
class Car(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    quantity = models.IntegerField()
    price = models.IntegerField()
    brand = models.ForeignKey(Brand,on_delete=models.SET_NULL,blank=True,null=True)
    image = models.ImageField(upload_to='documents/',blank=True,null=True)    
    author = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)