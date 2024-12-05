from django.http import HttpResponse
from django.shortcuts import render
 

def home(request):
    de = {
         'id': 'AN Mamun',
         'num':range(5), 
    }
    return render(request,'home.html',context=de)
    # return HttpResponse("Hello its a home page")
def footer(request):
    return render(request,'footer.html')