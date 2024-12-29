from django.db import models

# Create your models here.

class Brand(models.Model):
    name = models.CharField(max_length=20)
    details = models.TextField(max_length=200,null=True,blank=True)
    slug = models.SlugField(max_length=100,unique=True,null=True,blank=True)

    def __str__(self):
        return f"-{self.name}"