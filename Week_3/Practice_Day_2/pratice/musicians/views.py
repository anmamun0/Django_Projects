from django.shortcuts import render,redirect
from .forms import MusicianForm
from .models import Musician
from django.contrib import messages
# Create your views here.
def add_musician(request):
    if request.user.is_authenticated: 
        if request.method == "POST":
            form = MusicianForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,' successfull added..') 
                return render(request,'add_musician.html',{'form':form}) 
        else:
            form = MusicianForm() 
            return render(request,'add_musician.html',{'form':form})
    else:
        return redirect('homepage')
    
def edit_musician(request,id):
    if request.user.is_authenticated: 
        user = Musician.objects.get(pk=id)
        user_form = MusicianForm(instance=user)

        if request.method == "POST":
            user_form = MusicianForm(request.POST,instance=user)
            if user_form.is_valid():
                user_form.save()
                messages.success(request,'Musician Edit successfull')
                return redirect('add_musician') 
        return render(request,'add_musician.html',{'form':user_form})

    else:
        return redirect('homepage')

def delete(request,id):
    if request.user.is_authenticated: 
        user = Musician.objects.get(pk=id).delete()
        return  redirect('homepage')
    else:
        return redirect('homepage')