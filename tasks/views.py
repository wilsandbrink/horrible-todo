from django.shortcuts import render, HttpResponse, HttpResponseRedirect, reverse
from .models import Task


def index(request):
    tasks = Task.objects.all()

    context = {
        'tasks': tasks
    }
    template = 'tasks/index.html'

    return render(request, template, context)


def new_task(request):
    t = request.POST['title']
    new_task = Task(title = t)
    new_task.save()
    return HttpResponseRedirect(reverse('tasks:index'))


def task_change(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.is_done = not task.is_done
    task.save()
    return HttpResponseRedirect(reverse('tasks:index'))
