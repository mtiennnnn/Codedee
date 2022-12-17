from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from .models import User, Problem, Code
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm, UserForm
import sys
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import CodeSerializer
import os
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    return render(request, 'pages/home.html')

def about(request):
    user = User.objects.all().order_by('-points')
    context = {'users': user}
    return render(request, 'pages/about.html', context)

def rules(request):
    user = User.objects.all().order_by('-points')
    context = {'users': user}
    return render(request, 'pages/rules.html', context)

def loginPage(request):

    # delete message before load login page
    storage = messages.get_messages(request)
    for _ in storage:
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
    user = User.objects.all().order_by('-points')
    paginator = Paginator(user, 10)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)
    context = {'users': user, 'page_obj':page_obj}
    return render(request, 'pages/ranking.html', context)

def userProfile(request, username):
    user = User.objects.get(username=username)
    context = {'user': user}
    return render(request, 'pages/profile.html', context)

@login_required(login_url='login')
def problem_set(request):
    user = User.objects.all().order_by('-points')
    problem = Problem.objects.all().order_by('id')
    context = {'users': user, 'problems': problem}
    return render(request, 'pages/problem_set.html', context)

@login_required(login_url='login')
def problemPage(request, id):
    problem = Problem.objects.filter(id=id)
    # context = {'problems': problem}

    # code editor
    codeareadata = ""
    output = ""
    if request.method == "POST":
        codeareadata = request.POST['codearea']

        try:

            original_stdout = sys.stdout
            sys.stdout = open('file.txt', 'w') 

            exec(codeareadata) 

            sys.stdout.close()

            sys.stdout = original_stdout 

            output = open('file.txt', 'r').read()

        except Exception as e:
            sys.stdout = original_stdout
            output = e

    return render(request, 'pages/problem.html', {"problems": problem ,"code":codeareadata , "output":output})

@login_required(login_url='login')
def update_user(request):
    user = request.user
    form = UserForm(instance=user)
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile', username=user.username)

    return render(request, 'pages/update_user.html', {'form': form})

class submitCode(ListCreateAPIView):
    model = Code
    serializer_class = CodeSerializer

    def get_queryset(self):
        return Code.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = CodeSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'content' : 'context successful'
            }, status=status.HTTP_201_CREATED)
        
        return JsonResponse({
            'content': 'unsuccessful'
        }, status=status.HTTP_400_BAD_REQUEST)