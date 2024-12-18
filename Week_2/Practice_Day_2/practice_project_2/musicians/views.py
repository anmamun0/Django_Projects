from django.shortcuts import render,redirect
from .forms import MusicianForm
from .models import Musician
# Create your views here.
def home(request):
    if request.method == "POST":
        form = MusicianForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'add_musician.html',{'form':form})

    else:
        form = MusicianForm()

        return render(request,'add_musician.html',{'form':form})
    
def edit(request,id):
    user = Musician.objects.get(pk=id)
    user_form = MusicianForm(instance=user)

    if request.method == "POST":
        user_form = MusicianForm(request.POST,instance=user)
        if user_form.is_valid():
            user_form.save()
            return redirect('add_musician')
    
    return render(request,'add_musician.html',{'form':user_form})

def delete(request,id):
    user = Musician.objects.get(pk=id).delete()
    return  redirect('homepage')