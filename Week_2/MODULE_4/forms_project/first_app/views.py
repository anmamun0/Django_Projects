from django.shortcuts import render

from . forms import contactForm
# Create your views here.
def contact(request):
    if request.method == "POST": 
        name = request.POST.get("username")
        email = request.POST.get("email")
        select = request.POST.get('select')
        return render(request,'contact.html',{'name':name,'email':email,'select':select})
    else:
        return render(request,'contact.html')

def submit_form(request): 
    return render(request,'form.html')
def DjangoForm(request):
    form = contactForm(request.POST)
    if form.is_valid():
        print(form.cleaned_data)
    return render(request,'django_form.html',{'form':form})