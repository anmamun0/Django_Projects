from django.shortcuts import render , redirect
from . import models
# Create your views here.
def home(request):
    student = models.Student.objects.all()
     
    return render(request,'home.html',{'data':student})

def delete_student(request,roll):
    std = models.Student.objects.get(pk=roll).delete()
    st = models.Student.objects.filter(name_icontains ='v')
    # print(std)
    return redirect("home") 
