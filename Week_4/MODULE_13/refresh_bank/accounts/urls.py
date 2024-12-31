from django.contrib import admin
from django.urls import path , include
from .views import UserRegistrationView, UserLoginView, UserLogoutView, UserBankAccountUpdateView

urlpatterns = [
    path('register/',UserRegistrationView.as_view(),name='register'),
    path('login/',UserLoginView.as_view(),name='login'),
    path('logout/',UserLogoutView.as_view(),name='logout'),
    path('profile/',UserBankAccountUpdateView.as_view(),name='profile'),
]