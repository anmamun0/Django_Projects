from django.urls import path
from .views import profile_edit, profile
urlpatterns = [
    path('',profile,name='profile'),
    path('edit/',profile_edit,name='profile_edit'),
]