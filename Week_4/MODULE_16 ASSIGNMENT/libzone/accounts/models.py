from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    coin = models.IntegerField(default=0)
    registration_id = models.CharField(max_length=20)
    roll = models.CharField(max_length=10)
    department = models.CharField(max_length=100)
    session = models.CharField(max_length=20)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Profile of {self.user.username}"
