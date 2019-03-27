from django.shortcuts import render, HttpResponse


def index(request):
    return HttpResponse("You're at the todo index")
