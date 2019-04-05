from django.shortcuts import render, HttpResponse, HttpResponseRedirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .decorators import is_author

from .models import Task

# Todo: Learn how to comment code.
# Todo: Add teams.

@login_required
def index(request):
    """
    View that displays all the tasks belonging to a user.
    """
    tasks = Task.objects.filter(author=request.user).order_by('is_done')

    context = {
        'tasks': tasks
    }
    template = 'tasks/index.html'

    return render(request, template, context)


@login_required
def new_task(request):
    """
    View that creates a new task
    """
    t = request.POST['title']
    new_task = Task(title = t)
    new_task.author = request.user
    new_task.save()
    return HttpResponseRedirect(reverse('tasks:index'))


@login_required
@is_author
def task_change(request, task_id):
    """
    View that toggles a tasks is_done state
    """
    task = Task.objects.get(pk=task_id)
    # Toggle task state
    task.is_done = not task.is_done
    task.save()
    return HttpResponseRedirect(reverse('tasks:index'))


@login_required
@is_author
def task_delete(request, task_id):
    """
    View that deletes a task
    """
    task = Task.objects.get(pk=task_id)
    task.delete()

    messages.success(request, 'Task successfully deleted.')

    return HttpResponseRedirect(reverse('tasks:index'))
