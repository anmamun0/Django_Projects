from django.shortcuts import render
from .forms import Application_Form
# Create your views here.
def home(request):
    if request.method == "POST":
        application_form = Application_Form(request.POST,request.FILES)
        
        if application_form.is_valid():
            cv = application_form.cleaned_data['cv']
            # Save the file locally
            with open(f'./application/upload/{cv.name}', 'wb+') as destination:
                for chunk in cv.chunks():
                    destination.write(chunk)

            print(application_form.cleaned_data)
            return render(request,'application/home.html',{'application_form':application_form})
    else:
        application_form = Application_Form()
    return render(request,'application/home.html',{"application_form":application_form})
 

