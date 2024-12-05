from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('first_page/',views.first_page)
]