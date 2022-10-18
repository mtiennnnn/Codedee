from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request, 'pages/home.html')
def about(request):
    return render(request, 'pages/about.html')
def rules(request):
    return render(request, 'pages/rules.html')
def loginPage(request):
    context = {}
    return render(request, 'pages/login.html', context)
def register(request):
    # if request.method == 'POST':
    #     form = UserCreationForm(request.POST)
    #     if form.is_valid():
    #         form.save
    #         username = form.cleaned_data.get('username')
    #         messages.success(request, f'Hi {username}')
    #         return redirect('index')
    # else:
    #     form = UserCreationForm()
    #     return render(request, 'pages/register.html', {'form': form})

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        return render(request,'pages/index.html')
    else:
        form = UserCreationForm();
        return render(request, 'pages/register.html', {'form': form})
def ranking(request):
    return render(request, 'pages/ranking.html')
def problem_set(request):
    return render(request, 'pages/problem_set.html')