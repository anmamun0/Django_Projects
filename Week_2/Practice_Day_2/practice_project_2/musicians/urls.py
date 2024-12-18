from django.contrib import admin
from django.urls import path, include
from .views import home, edit, delete
urlpatterns = [
    path('add/',home,name='add_musician'),
    path('edit/<int:id>/',edit,name='edit'),
    path('delete/<int:id>/',delete,name='delete'),
]