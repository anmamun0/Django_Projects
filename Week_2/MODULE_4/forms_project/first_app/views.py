from django.shortcuts import render

from . forms import contactForm , StudentForm, PasswordValidationProject
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
    if request.method == "POST":
        form = contactForm(request.POST,request.FILES) 
        if form.is_valid():
            file = form.cleaned_data['file']
            with open('./first_app/upload/'+ file.name,'wb+') as destination:
                for chunck in file.chunks():
                    destination.write(chunck)
            print(form.cleaned_data)
            return render(request,'django_form.html',{'form':form})
 
    else:
        form = contactForm()
    return render(request,'django_form.html',{'form':form})

def studentForm(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return render(request,'student_form.html',{'form':form})

    else:
        form = StudentForm()
    return render(request,'student_form.html',{'form':form})

def PasswordValidation(request):
    if request.method == "POST":
        form = PasswordValidationProject(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return render(request,'password_validation.html',{'form':form})
    else:
        form = PasswordValidationProject()

    return render(request,'password_validation.html',{'form':form})
