from django.core.exceptions import PermissionDenied
from django.contrib import messages
from django.shortcuts import redirect
from .models import Task


def is_author(function):
    def wrap(request, *args, **kwargs):
        task = Task.objects.get(pk=kwargs['task_id'])
        if task.author == request.user:
            return function(request, *args, **kwargs)
        else:
            messages.error(request, 'What are you doing.')
            return redirect('tasks:index')
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
