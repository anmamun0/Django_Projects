from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import Task
# Create your views here.
def add_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_task')
    else:
        form = TaskForm()
        return render(request,'add_task.html',{'form':form})
    
def edit(request, id):
    task = Task.objects.get(pk=id)
    form = TaskForm(instance=task)

    if request.method == "POST":
        form = TaskForm(request.POST,instance=task)
        if form.is_valid():
            task.is_completed = True
            print(task.is_completed)
            form.save()
            return redirect('add_task')
    return render(request,'add_task.html',{'form':form})


def delete(request,id):
    task = Task.objects.get(pk=id).delete()
    return redirect('homepage') 