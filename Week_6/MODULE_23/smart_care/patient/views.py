from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
# Create your views here.
from .models import Patient
from .serializers import (
    PatientSerialier,
    RegistrationSerializer,
    UserLoginSerializer,
)
from rest_framework.response import Response

from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes

from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string

from django.contrib.auth.models import User
from django.shortcuts import redirect


from django.contrib.auth import authenticate ,logout , login 
from rest_framework.authtoken.models import Token

class PatientViewset(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerialier

# APIView -> django.views import views ar moto -> 12 batari

class UserRegistrationApiView(APIView):
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
            confirm_link = f"http://127.0.0.1:8000/patient/active/{uid}/{token}"
        
            email_subject = "Confirm Your Email! "
            email_body = render_to_string('confirm_email.html',{'confirm_link':confirm_link})

            email = EmailMultiAlternatives(
                subject=email_subject,
                body='',
                from_email= 'ReFresh Bank <noreply@example.com>', 
                to =[user.email]
            )
            email.attach_alternative(email_body, "text/html")
            email.send()

            return Response("Done")


        return Response(serializer.errors)
    

 
    

def activate(request,uid64,token):
    try:
        uid = urlsafe_base64_decode(uid64).decode()
        user = User._default_manager.get(pk=uid)
    except (User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user,token):
        user.is_active = True 
        user.save()
        return redirect('login')

    else:
        return redirect('register')
    
#  গোাল  আলু APIView
class UserLoignView(APIView):
    def post(self,request):
        serializer = UserLoginSerializer(data=self.request.data)
        if serializer.is_valid():
            username = serializer._validated_data['username']
            password = serializer._validated_data['password']

            user = authenticate(username=username,password=password)
             
            if user:
                token , _ = Token.objects.get_or_create(user=user)
                login(request,user)
                return Response({"token":token.key,"user_id":user.id,})
            else:
                return Response({"error":"Invalid Credential"})
        return Response(serializer.errors)

#  Nomaly post request ar jonnno API View use kora hoy

class UserLogoutView(APIView):
    def get(self,request):
        request.user.auth_token.delete()
        logout(request)
        return redirect('login')
