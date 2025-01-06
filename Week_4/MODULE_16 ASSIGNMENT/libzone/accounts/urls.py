from django.urls import path
from .views import RegistrationView ,UserLoginView ,user_logout

urlpatterns = [
    path('register/',RegistrationView.as_view(),name='register'),
    path('login/',UserLoginView.as_view(),name='login'),
    path('logout/',user_logout,name='logout'),
]