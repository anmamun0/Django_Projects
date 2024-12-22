from django.urls import path
from .views import signup,user_login,profile,user_logout,pass_change, pass_change2
urlpatterns = [
    path('signup/',signup,name='signup'),
    path('login/',user_login,name='login'),
    path('logout/',user_logout,name='logout'),
    path('profile/',profile,name='profile'),
    path('pass_change/',pass_change,name='passchange'),
    path('pass_change2/',pass_change2,name='passchange2'),
]