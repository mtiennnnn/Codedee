from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def index(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

def rules(request):
    return render(request, 'pages/rules.html')

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User or password does not exist!')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Please try again')

    context = {}
    return render(request, 'pages/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('index')

def registerPage(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()

            try:
                user = User.objects.get(username=username)
            except:
                messages.error(request, 'Username is already existed!')

            user.save()
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'An error was occurred, please try again!')

    return render(request, 'pages/register.html', {'form':form})

def ranking(request):
    return render(request, 'pages/ranking.html')

def userProfile(request, username):
    user = User.objects.get(username=username)
    context = {'user': user}
    return render(request, 'pages/profile.html', context)

@login_required(login_url='login')
def problem_set(request):
    return render(request, 'pages/problem_set.html')