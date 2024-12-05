from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    d = {
        'num':range(5)
    } 
    return render(request,'coding.html',context=d)
    # return HttpResponse('This is blog page')
