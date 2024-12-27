from django.shortcuts import render , redirect
from .forms import RegistrationForm, ChangeUserDataForm  
from django.contrib import messages

from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm , PasswordChangeForm, SetPasswordForm, PasswordResetForm
from django.contrib.auth import authenticate ,login, logout , update_session_auth_hash


from django.core.mail import send_mail , EmailMessage
from pratice.settings import EMAIL_HOST_USER


# Create your views here.
def custom_signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data['email']
                if User.objects.filter(email=email).exists():
                    messages.info(request,"You have a accout, please login")
                    return redirect('login')
                
                messages.success(request,'Account created..')
                form.save(commit=True)
                return render(request,'signup.html',{'form':form})
        else:
            form = RegistrationForm()
        return render(request,'signup.html',{'form':form})
    else:
        return redirect('homepage')
        
def custom_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = AuthenticationForm(request=request,data=request.POST)
            if form.is_valid():
                name = form.cleaned_data['username']
                userpass = form.cleaned_data['password']
                user = authenticate(username=name,password=userpass)
                if user is not None:
                    login(request,user) 
                    send_mail(
                        subject='Login Successfully',
                        message='Welcome back to login your profile',
                        from_email=EMAIL_HOST_USER,
                        recipient_list = ['anmamun0@gmail.com'],
                        fail_silently=False,
                    )
                    messages.success(request,'Login Successfully')
                    return redirect('profile')
                else:
                    messages.warning(request,'Login invalid!')
        else:
            form = AuthenticationForm()
        return render(request,'login.html',{'form':form})
    else:
        return redirect('homepage')
 
def custom_logout(request):
    logout(request)
    return redirect('login')


def custom_profile(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = ChangeUserDataForm(request.POST, instance = request.user)
            if form.is_valid():
                form.save() 
        else:
            form = ChangeUserDataForm(instance=request.user)
        return render(request,'profile.html',{'form':form}) 
    else:
        return redirect("homepage")

def cng_pass(request):
    if  request.user.is_authenticated:
        if request.method == "POST":
            form = PasswordChangeForm(user=request.user,data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request,form.user)
                messages.success(request,'Password Change successfull..')
                return redirect('profile')
        else:
            form = PasswordChangeForm(user=request.user)
            messages.warning(request,'unsuccessfull password change')

        return render(request,'password_cng.html',{'form':form})
    else:
        return render('homepage')
    
def cng_pass2(request):
    if  request.user.is_authenticated:
        if request.method == "POST":
            form = SetPasswordForm(user=request.user,data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request,form.user)
                messages.success(request,'Password Change successfull..')
                return redirect('profile')
        else:
            form = SetPasswordForm(user=request.user)
            messages.warning(request,'unsuccessfull password change')

        return render(request,'password_cng.html',{'form':form})
    else:
        return render('homepage')


# print all data of user --
# from django.contrib.auth.models import User
#  user = request.user
#         for field in User._meta.get_fields():
#             if hasattr(user, field.name):  # Ensure the field exists for the user
#                 value = getattr(user, field.name)
#                 print(f"{field.name}: {value}")
 

def send_email_info(request):
    if request.user.is_authenticated:
        message = f""

        user = request.user 
        for c in User._meta.get_fields():
            if hasattr(user,c.name):
                value = getattr(user,c.name)
                message += f"{c.name} : {value} \n" 

        html_content = """
        <html>
        <head>
            <style>
                .bg-primary {
                    background-color: #3490dc;
                    color: white;
                    padding: 1rem;
                    border-radius: 0.375rem;  }
                .text-center { text-align: center; }
                .text-xl { font-size: 1.25rem; }
            </style>
        </head>
        <body>
            <div class="bg-primary text-center text-xl">
                <p>Hello, {{ user.first_name }}! Your login information is ready.</p>
            </div>
        </body>
        </html>
        """
        send_mail(
            subject="Your login information.",
            message=message,
            from_email=EMAIL_HOST_USER,
            recipient_list=[request.user.email],
            fail_silently=False,
            html_message=html_content
        )

        return redirect('profile')
    else:
        return redirect("homepage")
    


import random 
from .forms import RequestOTPform , VerifyOPTForm
OTP_STORE = {}

def request_otp(request):
    if request.method == "POST":
        form = RequestOTPform(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']  # Access form data correctly
            if not User.objects.filter(email=email).exists():
                messages.warning(request, "This Email is not registered. Please signup.")
                return redirect("signup")

            otp = random.randint(int(1e5),int(1e6))
            OTP_STORE[email] = otp
            request.session['email'] = email

            send_mail(
                subject="Your OTP for Password Reset",
                message=f"Your OTP is {otp}. Please use this to reset your password.",
                from_email=  EMAIL_HOST_USER ,  # Replace with your email
                recipient_list=[email],
                fail_silently=False,
            )
            messages.success(request,"An OTP has been send in your mail")
            return redirect('verify_otp')
    else:
        form = RequestOTPform()
    return render(request,'forget/request_otp.html',{'form':form})


def verify_otp(request):
    email = request.session.get('email')
    if not email:
        messages.error(request,"Session expired or invalid, Please try agian.")
        return redirect("request_otp")

    if request.method == "POST":
        form = VerifyOPTForm(request.POST)
        if form.is_valid():
            entered_top = form.cleaned_data['otp']

            if email in OTP_STORE and OTP_STORE[email] == entered_top:
                del OTP_STORE[email]
                messages.success(request,"OTP Verified seccessfylly, Your can now reset your Password")
                return redirect('password_reset')
            else:
                messages.error(request,"Invalid OTP, Please Try agian!")
        
    else:
        form = VerifyOPTForm()
    return render(request,'forget/verify_top.html',{'form':form})

def password_reset(request):
    email = request.session.get('email')
    if not email:
        messages.error(request,"session expired or invalid, Please try agian.")
        return redirect("request_otp")

    try:
        user = User.objects.get(email=email)
        
    except User.DoesNotExist:
        messages.error(request,"User not Found , Please Try again")
        return redirect('request_otp')


    if request.method == "POST":
        form = SetPasswordForm(user=user,data=request.POST)
        if form.is_valid():
            form.save()

            del request.session['email']
            messages.success(request,"Your Password has hebb reset successfully")
            # login(request,user)
            return redirect('login')
    else:
        form = SetPasswordForm(user=user)
    return render(request,'forget/password_reset.html',{'form':form})                 




  