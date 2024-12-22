from django.shortcuts import render
from .forms import RegisterForm
# Create your views here.
from django.contrib import messages

def home(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            messages.success(request,"Account created successfully")
            # messages.warning(request,"Account created successfully")
            # messages.info(request,"Account created successfully")
             
            form.save(commit=True)
            print(form.cleaned_data)
    else:
        form = RegisterForm()
    return render(request,'home.html',{'form':form})