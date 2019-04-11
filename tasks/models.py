from django.db import models

from django.contrib.auth.models import User


class Task(models.Model):
    title = models.CharField(max_length=450)
    is_done = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
