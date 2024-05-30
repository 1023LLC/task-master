from django.shortcuts import render, redirect

from .models import Task

from .forms import TaskForm

def index(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            return redirect('/')
    else:
        form = TaskForm()
        
    tasks = Task.objects.filter(is_done=False)
    return render(request, 'task/index.html', {'tasks': tasks, 'form': form})


def delete(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.delete()
    
    return redirect('/')