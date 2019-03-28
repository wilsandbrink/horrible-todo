from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=450, required=True)
    is_done = models.BooleanField(default=False)
