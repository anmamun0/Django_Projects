from django.shortcuts import render 
from django.utils.timezone import now
from post.models import Post
from categories.models import Category

def home(request,category_slug=None):
    posts = Post.objects.all().order_by('-created_at')
    if category_slug is not None:
        cat = Category.objects.get(slug=category_slug)
        posts = Post.objects.filter(category=cat)

    categorys = Category.objects.all()

    context = {
        'posts':posts,
        'categorys':categorys,
    } 

    return render(request,'home.html',context)