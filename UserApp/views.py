from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Token, UserProfile  # Updated from UniqueLink to Token
from django.contrib.auth.views import LoginView

def home_view(request):
    return render(request, 'home.html')


def register(request, token=None):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            if token:
                try:
                    link = Token.objects.get(token=token)  # Updated from UniqueLink to Token
                    if not link.is_used:
                        link.user = user
                        link.is_used = True
                        link.save()
                        UserProfile.objects.create(user=user, role='JOB_SEEKER')
                except Token.DoesNotExist:  # Updated from UniqueLink to Token
                    return redirect('login')
            login(request, user)
            return redirect('home')
    else:
        if token:
            try:
                link = Token.objects.get(token=token)  # Updated from UniqueLink to Token
                if not link.is_used:
                    form = UserCreationForm()
                else:
                    return redirect('login')
            except Token.DoesNotExist:  # Updated from UniqueLink to Token
                return redirect('login')
        else:
            form = UserCreationForm()
    return render(request, 'UserApp/registration.html', {'form': form})


class UserLoginView(LoginView):
    template_name = 'UserApp/login.html'
