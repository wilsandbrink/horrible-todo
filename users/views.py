from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Todo: Subclass login view and add title

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
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
