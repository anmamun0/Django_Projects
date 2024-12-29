from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class History(models.Model):
    title = models.CharField(max_length=50)
    delevary_date = models.DateTimeField(auto_now_add=True)
    money = models.IntegerField()
    author = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True,related_name='history')
