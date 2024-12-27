from django.shortcuts import render ,redirect
from .forms import AlbumForm
from .models import Album
from django.contrib import messages
# Create your views here.
from musicians.models import Musician
def add_album(request):
    if request.user.is_authenticated: 
        if request.method == "POST":
            form = AlbumForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,'album Edit successfull') 
                return render(request,'add_album.html',{'form':form}) 
        else:
            form = AlbumForm() 
            return render(request,'add_album.html',{'form':form})
    else:
        return redirect('homepage')
def edit_album(request,id):
    if request.user.is_authenticated: 
        albm = Album.objects.get(pk=id)
        form = AlbumForm(instance=albm)
        if request.method == "POST":
            form = AlbumForm(request.POST, instance=albm)
            if form.is_valid():
                form.save()
                messages.success(request,'edit successfull') 
                return redirect('homepage')
        return render(request,'edit_album.html',{'form':form})
    else:
        return redirect('homepage')
    

def delete_album(request,id):
    if request.user.is_authenticated: 
        Album.objects.get(pk=id).delete()
        messages.success(request,'deleted album')

        return redirect('homepage')
    else:
            return redirect('homepage')