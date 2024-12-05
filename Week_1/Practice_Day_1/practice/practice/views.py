from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
def home(request):
    d = {
        'dic':[
            {
                'name': 'zed', 
                'age': 19
            },
            {
                'name': 'amy', 
                'age': 22
            },
            {
                'name': 'joe', 
                'age': 31
            },
        ],
        'my_date':datetime.now(),
        'lst':[1,2,3,4,5],
    }
    return render(request,'home.html',context=d)

    return HttpResponse("This is home working!")

def contact(request):
    return render(request,'contact.html')