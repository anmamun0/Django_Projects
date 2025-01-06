from django.db import models 
# Create your models here.
from .constants import TRANSACTION_TYPE
from django.contrib.auth.models import User

from accounts.models import StudentProfile
from books.models import Book

class Transaction(models.Model):
    profile = models.ForeignKey(StudentProfile, related_name = 'transactions', on_delete = models.CASCADE)  
    book = models.ForeignKey(Book,related_name='viewer',on_delete=models.CASCADE,null=True, blank=True)
    coin = models.IntegerField()
    coin_after_transaction = models.DecimalField(decimal_places=2, max_digits = 12)
    transaction_type = models.IntegerField(choices=TRANSACTION_TYPE, null = True)
    timestamp = models.DateTimeField(auto_now_add=True) 
    
    class Meta:
        ordering = ['-timestamp'] 