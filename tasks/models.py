from django.db import models

from django.contrib.auth.models import User

# Work in progress

class Organization(models.Model):
    name = models.CharField(max_length=450)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    members = models.ManyToManyField(User)


class Project(models.Model):
    owner = models.ForeignKey(Organization)
    title = models.CharField(max_length=450)


class Task(models.Model):
    title = models.CharField(max_length=450)
    is_done = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
