from django.core.exceptions import PermissionDenied
from .models import Task


def is_author(function):
    def wrap(request, *args, **kwargs):
        task = Task.objects.get(pk=kwargs['task_id'])
        if task.author == request.user:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
