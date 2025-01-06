from django.shortcuts import render , redirect
from django.views.generic import CreateView , FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, logout

from django.urls import reverse_lazy
# Create your views here.
from .forms import RegistraionForm 
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.template.loader import render_to_string

from core.constants import send_email

class RegistrationView(FormView):
    template_name = 'accounts/registration.html'
    form_class = RegistraionForm
    success_url = reverse_lazy('home')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        messages.success(self.request,"Membership successfull.")

        return super().form_valid(form)

class UserLoginView(LoginView):
    template_name = 'accounts/login.html'
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)
    def get_success_url(self):

        context = {
            'user':self.request.user, 
        }
        body = render_to_string('email_templates/login_email.html',context)

        messages.success(self.request,"Login successfull.") 
        send_email(self.request.user,"Login Successfull",body)
        return reverse_lazy('home')

def user_logout(request):
    if request.user.is_authenticated:
        logout(request) 
    return redirect('home')