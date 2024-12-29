from django.db import models
from django.contrib.auth.models import User
from cars.models import Car
# Create your models here.
class Comment(models.Model):
    post = models.ForeignKey(Car,on_delete=models.CASCADE,related_name='comment',null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    commented_user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='comment_user_info',null=True,blank=True)
