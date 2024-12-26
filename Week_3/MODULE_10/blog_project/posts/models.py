from django.db import models
from categories.models import Category
# from author.models import Author
from django.contrib.auth.models import User
from django.utils.timezone import now
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    category = models.ManyToManyField(Category) # akta post multiple categorir modda thakta para aber akta categorir modda multiple post takta pare

    author = models.ForeignKey(User,on_delete=models.CASCADE,null=True) # Many to one -> onek gulu post ar akta author thaka,

    created_at = models.DateTimeField(default=now, editable=False)  # Auto-set to current time on creation

    def __str__(self):
        return self.title 