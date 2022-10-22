from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm
# Create your views here.

def index(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

def rules(request):
    return render(request, 'pages/rules.html')

def loginPage(request):

    # delete message before load login page
    storage = messages.get_messages(request)
    for _ in storage:
        # This is important
        # Without this loop `_loaded_messages` is empty
        pass

    for _ in list(storage._loaded_messages):
        del storage._loaded_messages[0]


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
    # form = UserCreationForm()
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, form.errors.as_data)

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

@login_required(login_url='login')
def update_user(request):
    return render(request, 'pages/update_user.html')