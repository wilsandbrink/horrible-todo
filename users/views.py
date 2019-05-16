from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Todo: Subclass login view and add title

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(request, 'Successfully registered')

            return redirect('tasks:index')
    else:
        form = UserCreationForm()

    context = {
        'form': form,
        'title': 'Register'
    }
    template = 'users/register.html'

    return render(request, template, context)


@login_required
def profile(request):
    user = request.user

    context = {
        'user': user,
        'title': 'Profile'
    }
    template = 'users/profile.html'

    return render(request, template, context)
