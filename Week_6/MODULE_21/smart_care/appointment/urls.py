from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import AppointmentViewset

router = DefaultRouter()

router.register('',AppointmentViewset)


urlpatterns = [
    path('',include(router.urls)),
]

