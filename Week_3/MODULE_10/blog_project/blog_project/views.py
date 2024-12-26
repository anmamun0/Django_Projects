from django.shortcuts import render
from posts.models import Post
from django.utils.timezone import now

def home(request):
    data = Post.objects.all().order_by('-created_at')

    for post in data:
        post.days_passed = (now() - post.created_at).days

    for i in data:
        print(i.title)
        for j in i.category.all():
            print(j)

    return render(request,'home.html',{'data':data})