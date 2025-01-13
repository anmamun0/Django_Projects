from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
# Create your views here.
from .models import Patient
from .serializers import (
    PatientSerialier,
    RegistrationSerializer
)
from rest_framework.response import Response

from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes


class PatientViewset(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerialier

# APIView -> django.views import views ar moto -> 12 batari

class UserRegistration(APIView):
    serializer_class = RegistrationSerializer

    def post(self,requert):
        serializer = self.serializer_class(data=requert.data)
        
        if serializer.is_valid():
            user = serializer.save() 
            print(user)
            token = default_token_generator.make_token(user)
            print(token)
            uid = urlsafe_base64_encode(force_bytes(user.pk)) # unique url make kora
            print("UID: ",uid)
            confirm_link = f"http://127:0.0.1:800:/patient/active/{uid}/{token}"
            return Response("Done")
        
            email_subject = "Confirm Your Email! "
            email_body = render_to_string('')

        return Response(serializer.errors)
    
 