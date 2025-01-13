from django.shortcuts import render
from rest_framework import viewsets
from .models import (
    Specialization,
    Designation,
    AvailableTime,
    Doctor,
    Review
)

from .serializers import (
    SpecializationSerialier,
    DesignationSerialier,
    AvailableTimeSerialier,
    DoctorSerialier,
    ReviewSerialier,
)

# Create your views here.

class DoctorViewset(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerialier

class SpecializationViewset(viewsets.ModelViewSet):
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerialier

class DesignationViewset(viewsets.ModelViewSet):
    queryset = Designation.objects.all()
    serializer_class = DesignationSerialier

class AvailableTimeViewset(viewsets.ModelViewSet):
    queryset = AvailableTime.objects.all()
    serializer_class = AvailableTimeSerialier
    
class ReviewViewset(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerialier