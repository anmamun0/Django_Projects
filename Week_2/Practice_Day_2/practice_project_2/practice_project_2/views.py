from django.shortcuts import render, redirect
from musicians.models import Musician
from albums.models import Album
def home(request):
    data = Musician.objects.all()
    albums = Album.objects.all()

    return render(request,'home.html',{'data':data,'albums':albums})