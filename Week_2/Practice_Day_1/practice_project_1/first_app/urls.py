from django.urls import path
from .views import home ,ErrorPage

urlpatterns = [
    path('',home,name='homepage'),
    path('error',ErrorPage,name='errorpage'),
]