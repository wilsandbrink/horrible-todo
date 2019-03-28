from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=450)
    is_done = models.BooleanField(default=False)
