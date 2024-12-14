from django.db import models

# Create your models here.
class StudentModel(models.Model):
    roll = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    father_name = models.CharField(max_length=30)
    address = models.TextField()
    # price = models.DecimalField(max_digits=10, decimal_places=2)      
    is_available = models.BooleanField(default=True)
    cover_image = models.ImageField(upload_to='uploads/')
    cv = models.FileField(upload_to='uploads/')

    def __str__(self):
        return f"{self.roll}: {self.name}"
    