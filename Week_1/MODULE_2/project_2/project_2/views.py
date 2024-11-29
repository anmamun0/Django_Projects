from django.http import HttpResponse
from django.shortcuts import render

# def index(request):
    # return HttpResponse("This is main")

def index(request):
    return render(request,'index.html')