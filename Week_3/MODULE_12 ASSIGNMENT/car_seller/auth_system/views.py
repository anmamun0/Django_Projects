from django.shortcuts import render , redirect
from .forms import RegistrationForm, ChangeUserDataForm  
from django.contrib import messages

from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm , PasswordChangeForm, SetPasswordForm, PasswordResetForm
from django.contrib.auth import authenticate ,login, logout , update_session_auth_hash


from django.core.mail import send_mail , EmailMessage
from car_seller.settings import EMAIL_HOST_USER

from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView

from django.views.generic.edit import FormView , UpdateView
from django.urls import reverse_lazy , reverse

from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin 

from django.views import View
from .models import History
from cars.models import Car
# Create your views here.
class CustomRegisterView(FormView):
    template_name = 'signup.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('profile')

    def dispatch(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('homepage')
        return super().dispatch(request,*args,**kwargs)
    def form_valid(self,form):
        email = form.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            messages.info(self.request,"You have a account, please login")
            return redirect('login')
        
        form.save()
        messages.success(self.request,"Account created..")
        return super().form_valid(form)
    
    def form_invalid(self,form):
        messages.error(self.request,'error info')
        return super().form_invalid(form)
     
class CustomLoginView(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        # You can add custom logic, such as logging or sending emails
        messages.success(self.request,'Login Successfull!')
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.warning(self.request,"Invalid information")
        return super().form_invalid(form)
    
    def get_success_url(self):
        return reverse('profile')
 
class CustomLogoutView(LogoutView):
    next_page = 'login'
 
def custom_logout(request):
    logout(request)
    return redirect('login')


class ProfileView(LoginRequiredMixin,TemplateView):
    template_name = 'profile.html'
    login_url = "/user/login/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['yoyo'] = "its brand name"
        user = self.request.user
        context['historys'] = self.request.user.history.all()
        context['cars'] = Car.objects.filter(author=user)
 

        return context
 

class EditProfileView(LoginRequiredMixin,UpdateView):
    model = User
    form_class = ChangeUserDataForm
    template_name = 'edit_profile.html'
    success_url = reverse_lazy('profile')
 
    def form_valid(self,form):
        messages.success(self.request,"Profile edit successfull.")
        return super().form_valid(form)
    
    def get_object(self,queryset=None):
        return self.request.user
 

class ChangePasswordView(LoginRequiredMixin,PasswordChangeView):
    template_name = 'password_cng.html'
    form_class = PasswordChangeForm
    success_url = reverse_lazy('profile')

    def form_valid(self,form):
        update_session_auth_hash(self.request,form.user)
        messages.success(self.request,"Password cng successfull!")
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.warning(self.request,"Invalid form data! ")
        return super().form_invalid(form)

class ChangePasswordView2(LoginRequiredMixin,PasswordChangeView):
    template_name = 'password_cng.html'
    form_class = SetPasswordForm
    success_url = reverse_lazy('profile')

    def form_valid(self,form):
        update_session_auth_hash(self.request,form.user)
        messages.success(self.request,"Password cng successfull!")
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.warning(self.request,"Invalid form data! ")
        return super().form_invalid(form)
  


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




# View class or a mix of FormView and TemplateView if needed.
class PasswordResetView(View):
    template_name = 'forget/password_reset.html'

    def dispatch(self, request, *args, **kwargs):
        email = request.session.get('email')
        if not email:
            messages.error(request,'Session expired!')
            return redirect('request_otp')
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request,"User not found")
            return redirect('request_otp')
        self.user = user 

        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = SetPasswordForm(user=self.user)
        return render(request, self.template_name, {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = SetPasswordForm(user=self.user, data=request.POST)
        if form.is_valid():
            form.save()
            del request.session['email']  # Clear email from session
            messages.success(request, "Your password has been reset successfully.")
            return redirect('login')
        return render(request, self.template_name, {'form': form})
 


  