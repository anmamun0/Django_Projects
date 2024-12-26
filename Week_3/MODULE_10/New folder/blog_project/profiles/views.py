from django.shortcuts import render , redirect

from .forms import ProfileForm
# Create your views here.
from post.models import Post 

def profile(request):
    posts = Post.objects.filter(author=request.user).order_by('-created_at')
    data = {
        'posts':posts, 
    }
    return render(request,'profile.html',data)

def profile_edit(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = ProfileForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                return redirect('profile_edit')
        else:
            form = ProfileForm(instance=request.user)

        return render(request,'profile_edit.html',{"form":form})
    else:
        return redirect('login')
 