from django.db import models 
# Create your models here.
class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=11)
    CHOICE_INSTRUMENT = [
        ('piano','Piano'),
        ('drumno','Drum'),
        ('violin','Violin'),
        ('flute','Flute'),
        ('guitat','Guitat'),
    ]
    instrument_type = models.CharField(
        max_length=200,
        choices=CHOICE_INSTRUMENT
    ) 
    
    def __str__(self):
        return f"{self.first_name} \t| {self.instrument_type}"
