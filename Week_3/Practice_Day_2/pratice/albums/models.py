from django.db import models
from musicians.models import Musician
# Create your models here.
class Album(models.Model):
    album_name = models.CharField(max_length=20)
    release_date = models.DateField() 
    CHOICE_RATING = [
        ('1star','1-star'),
        ('2star','2-star'),
        ('3star','3-star'),
        ('4star','4-star'),
        ('5star','5-star'),
    ]
    instrument_type = models.CharField(
        max_length=200,
        choices=CHOICE_RATING
    )

    musician = models.ForeignKey(Musician,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return f"{self.album_name} \t| {self.release_date}"
