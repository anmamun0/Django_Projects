from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    # return HttpResponse("This is first app home")
    return render(request,'first_app/home.html')

