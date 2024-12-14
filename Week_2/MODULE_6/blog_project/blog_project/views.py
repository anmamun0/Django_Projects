from django.shortcuts import render
from posts.models import Post

def home(request):
    data = Post.objects.all()
    for i in data:
        print(i.title)
        for j in i.category.all():
            print(j)

    return render(request,'home.html',{'data':data})