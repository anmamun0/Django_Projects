from django.shortcuts import render
from .forms import AlbumForm
# Create your views here.
def home(request):
    if request.method == "POST":
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'add_album.html',{'form':form})

    else:
        form = AlbumForm()

        return render(request,'add_album.html',{'form':form})
    
