from django.urls import path
from .views import custom_signup , custom_login , custom_profile, custom_logout, cng_pass, cng_pass2 ,send_email_info,request_otp,verify_otp,password_reset

from django.contrib.auth import views as auth_views
urlpatterns = [
    path('login/',custom_login,name='login'),
    path('logout/',custom_logout,name='logout'),
    path('profile/',custom_profile,name='profile'),
    path('signup/',custom_signup,name='signup'),
    path('password_cng/',cng_pass,name='password_cng'),
    path('password_cng2/',cng_pass2,name='password_cng2'), 
    path('send_email_info/',send_email_info,name='send_email_info'), 

    # OTP field
    path('request_otp/', request_otp, name='request_otp'),
    path('verify_otp/',  verify_otp, name='verify_otp'),
    path('password_reset/', password_reset, name='password_reset'),

]