from django.urls import path
from . import views 
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('login/',views.CustomLoginView.as_view(),name='login'),
    path('logout/',views.custom_logout,name='logout'),
    path('signup/',views.CustomRegisterView.as_view(),name='signup'),

    path('profile/',views.ProfileView.as_view(),name='profile'), 
    path('edit_profile/',views.EditProfileView.as_view(),name='edit_profile'),

    path('password_cng/',views.ChangePasswordView.as_view(),name='password_cng'),
    path('password_cng2/',views.ChangePasswordView2.as_view(),name='password_cng2'), 
    
    path('send_email_info/',views.send_email_info,name='send_email_info'), 

    # OTP field
    path('request_otp/', views.request_otp, name='request_otp'),
    path('verify_otp/',  views.verify_otp, name='verify_otp'),
    path('password_reset/', views.PasswordResetView.as_view(), name='password_reset'),

]