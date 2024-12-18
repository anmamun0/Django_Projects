from django.db import models
from category.models import Category
from datetime import datetime
# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    assign_date = models.DateField(default=datetime.now())
    
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.title