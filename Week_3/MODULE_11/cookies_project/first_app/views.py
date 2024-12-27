from django.shortcuts import render
from datetime import datetime, timedelta

# Create your views here.
def home(request):
    response = render(request,'home.html')
    # response.set_cookie('name','AN_Mamun',max_age=60)
    response.set_cookie('name','AN_Mamun',expires=datetime.utcnow()+timedelta(days=7))
    return response
    # return render(request,'home.html')

def get_cookie(request):
    name = request.COOKIES.get('name')

    print(request.COOKIES)
    for x in request.COOKIES:
        print(x)

    return render(request,'get_cookie.html',{'name':name})

def delete_cookie(request):
    response = render(request,'del.html')
    response.delete_cookie('name')
    return response


def set_session(request):
    data = {
        'name':'anmamun0',
        'age':20,
        'language':'English'
    }
    request.session.update(data)
    request.session.set_expiry(10)
    return render(request,'home.html')

def get_session(request):
    data = request.session

    # del request.session['name']
    # request.session.flush()

    return render(request,'get_session.html',{'data':data})