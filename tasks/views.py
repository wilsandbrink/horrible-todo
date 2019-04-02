from django.shortcuts import render, HttpResponse, HttpResponseRedirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Task


@login_required
def index(request):
    tasks = Task.objects.filter(author=request.user)

    context = {
        'tasks': tasks
    }
    template = 'tasks/index.html'

    return render(request, template, context)


def new_task(request):
    t = request.POST['title']
    new_task = Task(title = t)
    new_task.author = request.user
    new_task.save()
    return HttpResponseRedirect(reverse('tasks:index'))


def task_change(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.is_done = not task.is_done
    task.save()
    return HttpResponseRedirect(reverse('tasks:index'))


def task_delete(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.delete()

    messages.success(request, 'Task successfully deleted.')

    return HttpResponseRedirect(reverse('tasks:index'))
