from django.contrib import admin
from django.db import models
from .models import Category
# Register your models here.
# admin.site.register(models.Category)

# class CategoryAdmin(admin.ModelAdmin):
#     prepopulated_fields = {'slug':('name',)}
#     list_display = ['name','slug']

admin.site.register(Category)
