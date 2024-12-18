from django.contrib import admin
from django.urls import path, include
from .views import home
urlpatterns = [
    path('add/',home,name='add_album'),
]