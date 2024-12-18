from django.urls import path
from .views import add_category
urlpatterns = [
    path('add_category/',add_category,name='add_category'),

]