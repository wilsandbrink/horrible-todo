from django.http import JsonResponse
from tasks.models import Task


def index(request):
    tasks = Task.objects.all()

    return JsonResponse({'tasks': tasks})
