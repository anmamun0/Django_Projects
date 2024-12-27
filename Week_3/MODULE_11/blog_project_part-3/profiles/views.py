from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required

from .forms import ProfileForm
# Create your views here.
from post.models import Post 

@login_required(login_url='/user/login/')
def profile(request):
    posts = Post.objects.filter(author=request.user).order_by('-created_at')
    data = {
        'posts':posts, 
    }
    return render(request,'profile.html',data)

@login_required(login_url='/user/login/')
def profile_edit(request):
        if request.method == "POST":
            form = ProfileForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                return redirect('profile_edit')
        else:
            form = ProfileForm(instance=request.user)

        return render(request,'profile_edit.html',{"form":form})
 