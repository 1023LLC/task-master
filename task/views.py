from django.shortcuts import render

from .models import Task

def index(request):
    tasks = Task.objects.filter(is_done=False)
    return render(request, 'task/index.html', {'tasks': tasks})