from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    
    return HttpResponse("This is blog page")

def first_page(request):
    return render(request,'first_page.html')