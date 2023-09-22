# filo_project/UserApp/views.py

from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Token, UserProfile
from django.contrib.auth.views import LoginView




def home_view(request):
    return render(request, 'home.html')



def register(request, token=None):
    if token is None:
        messages.error(request, 'Registration is only allowed through a valid invitation link.')
        return redirect('login')

    try:
        link = Token.objects.get(token=token)
        if link.is_used:
            messages.error(request, 'This invitation link has already been used.')
            return redirect('login')
    except Token.DoesNotExist:
        messages.error(request, 'Invalid invitation link.')
        return redirect('login')
        
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            link.is_used = True
            link.save()
            UserProfile.objects.create(user=user, role='JOB_SEEKER')
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'UserApp/registration.html', {'form': form})


class UserLoginView(LoginView):
    template_name = 'UserApp/login.html'
