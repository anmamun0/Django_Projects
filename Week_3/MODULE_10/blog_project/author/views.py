from django.shortcuts import render, redirect
from .forms import   RegisterForm , OTPRequestForm , OTPVerifyForm

from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm , SetPasswordForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.mail import send_mail


# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request,'register.html',{'form':form})



def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=name,password=password)
            if user is not None:
                messages.success(request,"Login Successfyll..")
                login(request,user)
                return redirect('homepage')
            else:
                messages.warning(request,"Your are not authenticated people, we can ban account..")
    else:
        form = AuthenticationForm(request=request)
    return render(request,'login.html',{'form':form})



def logout_user(request):
    logout(request)
    return redirect('homepage')


import random
from blog_project.settings import EMAIL_HOST_USER
OTP_BANK = {}

def request_otp(request):
    if request.method == "POST":
        form = OTPRequestForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if not User.objects.filter(email=email).exists():
                messages.error(request,"Your mail not exist..")
                # return redirect('signup')
            else:
                otp = random.randint(int(1e5),int(1e6))
                request.session['email'] = email
                OTP_BANK[email] = otp

                send_mail(
                    subject='OTP from Django Site',
                    message= f"Your One-Time Password  {otp}  Please use this to reset your password. \n Note: This OTP is valid for 5 minutes.",
                    from_email= 'an.Django <noreply@example.com>',
                    recipient_list=[email],
                    fail_silently=False,
                )
                return redirect('verify_otp')
    else:
        form = OTPRequestForm(request.POST)
    return render(request,'otp_verification/request_otp.html',{'form':form})

def verify_otp(request):
    if request.method == "POST":
        form = OTPVerifyForm(request.POST)
        if form.is_valid():
            email = request.session['email']
            enter_otp = form.cleaned_data['otp']

            if email in OTP_BANK and OTP_BANK[email]== enter_otp:
                del OTP_BANK[email]
                messages.success(request,"Login Successfull.")
                return redirect("reset_password")
            else:
                return redirect('request_otp')
    else:
        form = OTPVerifyForm()
    return render(request,'otp_verification/request_otp.html',{'form':form})

def reset_password(request):
    email = request.session['email']
    if not email:
        messages.error(request,'session expaired and invalid, Please try again')
    
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        messages.error("User doest exist, invalid!")
        return redirect('request_otp')

    if request.method == "POST":
        form = SetPasswordForm(user=user,data=request.POST)
        if form.is_valid():
            form.save()
            del request.session['email']
            messages.success(request,"Reset Password Successfull")
            login(request,user)
            return redirect('homepage')
    else:
        form = SetPasswordForm(user=user)
    return render(request,'otp_verification/reset_password.html',{'form':form})