from django.shortcuts import render , redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
 
from .forms import DjangoForm, ContactForm

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = DjangoForm(request.POST)
        if form.is_valid():
            return render(request,'home.html',{'form':form})
    else:
        form = DjangoForm()
        return render(request,'home.html',{'form':form})

 
def ErrorPage(request):
    return render(request,'error.html')



def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = 'ContactForm'
            body = {
                'name': form.cleaned_data['name'], 
                'description': form.cleaned_data['description'], 
                'email': form.cleaned_data['email'], 
            }      
            message = "\n".join(body.values()) 
            try:
                send_mail(subject, message, 'almamun20044@gmail.com', ['anmamun0@gmail.com'])
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return redirect('homepage')
    else:
        form = ContactForm()

    return render(request, 'home.html', {'form': form})
