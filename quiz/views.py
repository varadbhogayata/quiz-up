from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'quiz/index.html', context=None)

@login_required(login_url='login')
def user_home(request):
    return render(request, 'quiz/user_home.html', context=None)

@login_required(login_url='login')
def leaderboard(request):
    return render(request, 'quiz/leaderboard.html', context=None)

@login_required(login_url='login')
def play(request):
    return render(request, 'quiz/play.html', context=None)