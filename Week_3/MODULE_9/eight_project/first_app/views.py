from django.shortcuts import render
from .forms import RegisterForm
# Create your views here.
def home(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
    else:
        form = RegisterForm()
    return render(request,'home.html',{'form':form})