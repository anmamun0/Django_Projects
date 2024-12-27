from django.urls import path, include

from .views import register , login_user ,logout_user,request_otp,verify_otp,reset_password,UserLoginView

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register/',register, name="register"),
    # path('login/',login_user, name="login"), 
    path('login/',UserLoginView.as_view(), name="login"), 
    path('logout/',logout_user, name="logout"), 
    # path('logout/',LogoutView.as_view(), name="logout"), 

    path('request_otp/',request_otp,name='request_otp'),
    path('verify_otp/',verify_otp,name='verify_otp'),
    path('reset_password/',reset_password,name='reset_password'),

    
]