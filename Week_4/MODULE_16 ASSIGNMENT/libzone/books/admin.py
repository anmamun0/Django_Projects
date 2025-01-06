from django.contrib import admin
from .models import Book,Category
# Register your models here.
admin.site.register(Book)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ['name','slug']
    
admin.site.register(Category,CategoryAdmin)