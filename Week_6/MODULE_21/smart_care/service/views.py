from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from .models import Service
from .serializers import ServiceSerializer

class ServiceViewset(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    
