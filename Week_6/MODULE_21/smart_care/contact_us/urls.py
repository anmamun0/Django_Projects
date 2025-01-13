from rest_framework.routers import DefaultRouter
from django.urls import path , include
from .views import ContactusViewset
router = DefaultRouter() # amader router

router.register(r'',ContactusViewset) # router ar antena

urlpatterns = [
    path('',include(router.urls)),

]