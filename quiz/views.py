from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import UserLoginForm, RegistrationForm


# Create your views here.
def index(request):
    return render(request, 'quiz/index.html', context=None)


def login_request(request):
    title = "Login"
    form = UserLoginForm(request.POST or None)
    context = {
        'form': form,
        'title': title,
    }
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)

        login(request, user)
        # messages.info(request, f"You are now logged in  as {user}")
        return redirect('user-home')
    else:
        print(form.errors)
        # messages.error(request, 'Username or Password is Incorrect! ')
    return render(request, 'quiz/login.html', context=context)


def signup_request(request):
    title = "Create Account"
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()

    context = {'form': form, 'title': title}
    return render(request, 'quiz/signup.html', context=context)


def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect('index')


@login_required(login_url='login')
def user_home(request):
    return render(request, 'quiz/user_home.html', context=None)

@login_required(login_url='login')
def leaderboard(request):
    return render(request, 'quiz/leaderboard.html', context=None)

@login_required(login_url='login')
def play(request):
    return render(request, 'quiz/play.html', context=None)