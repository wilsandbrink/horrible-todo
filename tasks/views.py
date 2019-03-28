from django.shortcuts import render, HttpResponse
from .models import Task


def index(request):
    tasks = Task.objects.all()

    context = {
        'tasks': tasks
    }
    template = 'tasks/index.html'

    return render(request, template, context)
