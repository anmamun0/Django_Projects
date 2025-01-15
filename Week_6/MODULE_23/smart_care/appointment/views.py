from django.shortcuts import render
from rest_framework import viewsets 
# Create your views here.
from .models import Appointment
from .serializers import AppointmentSerializer

class AppointmentViewset(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    #custom query kortaci
    def get_queryset(self):
        queryset = super().get_queryset()
        patient_id = self.request.query_params.get('patient_id')
        print(self.request.query_params)
        
        if patient_id:
            queryset = queryset.filter(patient_id=patient_id)
            return queryset