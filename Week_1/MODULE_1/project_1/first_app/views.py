from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def courses(request):
    return HttpResponse("THis is first app")


def home(request):
    return HttpResponse("this is First app home page..")