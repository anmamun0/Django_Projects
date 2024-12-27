from django.contrib import admin
from django.urls import path, include
from .views import add_musician, edit_musician, delete
urlpatterns = [
    path('add/',add_musician,name='add_musician'),
    path('editt/<int:id>/',edit_musician,name='edit_musician'),
    path('delete/<int:id>/',delete,name='delete'),
]