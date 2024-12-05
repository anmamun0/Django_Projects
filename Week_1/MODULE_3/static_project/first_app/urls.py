from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name = 'home'),
    path('about/<int:id>/',views.about, name = 'about')
]