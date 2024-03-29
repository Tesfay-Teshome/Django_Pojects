from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
from .forms import CreateTask

# Create your views here.
def index(request):
    tasks = Task.objects.all()
    form = CreateTask()
    if request.method == 'POST':
        form = CreateTask(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    context = {'tasks': tasks, 'form': form}
    return render(request,'tasks/index.html', context)

def Upload_Task(request):
    upload = CreateTask()
    if request.method == 'POST':
        upload = CreateTask(request.POST)
        if upload.is_valid():
            upload.save()
            return redirect("/")
    context = {'upload': upload}
    return render(request, 'tasks/upload.html', context)

def Update_Task(request, pk):
    task = Task.objects.get(id=pk)
    form = CreateTask(instance=task)
    if request.method == 'POST':
        form = CreateTask(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("/")
    context = {'task': task,'form': form}
    return render(request, 'tasks/update.html', context)

def Delete_Task(request, pk):
    item = Task.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect("/")
    context = {'item': item}
    return render(request, 'tasks/delete.html', context)
