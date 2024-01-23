from django.shortcuts import render, redirect
from task.forms import TaskForm
from . import models
# Create your views here.

def task(request):
    if request.method == 'POST':
        data = TaskForm(request.POST)
        if data.is_valid():
            data.save()
            return redirect('task')
    
    else:
        data = TaskForm()
    return render(request, 'task.html', {'form':data})

def edit(request, id):
    task_ob = models.Task.objects.get(pk=id)
    data = TaskForm(instance=task_ob)
    if request.method == 'POST':
        data = TaskForm(request.POST, instance=task_ob)
        if data.is_valid():
            data.save()
            return redirect('home')
        
    return render(request, 'task.html', {'form':data})

def delete(request, id):
    task_ob = models.Task.objects.get(pk=id)
    task_ob.delete()
    return redirect('home')