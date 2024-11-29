from django.shortcuts import render
from datetime import datetime


# Create your views here.
def home(request):
    # dictionary format

    d = {
        'author':'AN Mamun ',
        'age':15,
        'lst': ['python','is','fun'],
        'date':datetime.now(),
        'courses':[ {
                'id':1,
                'name':'python',
                'fee':400
            },
            {
                'id':2,
                'name':'Django',
                'fee':500
            },
            {
                'id':5,
                'name':'Tkinter',
                'fee':10000
            }
        ]
    }
    return render(request,'home.html',context=d)