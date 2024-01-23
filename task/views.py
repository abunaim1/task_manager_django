from django.shortcuts import render, redirect
from task.forms import TaskForm
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