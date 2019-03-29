from django.http import JsonResponse
from tasks.models import Task

# Will probably replace this with the DRF

def index(request):
    tasks = Task.objects.all().values()

    return JsonResponse({'tasks': 'nothing here xddd'})
