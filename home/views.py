from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from .models import User, Problem
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm, UserForm
import sys
import os
from django.core.paginator import Paginator
from io import StringIO

# Create your views here.


def index(request):
    return render(request, "pages/home.html")


def about(request):
    user = User.objects.all().order_by("-points")
    context = {"users": user}
    return render(request, "pages/about.html", context)


def rules(request):
    user = User.objects.all().order_by("-points")
    context = {"users": user}
    return render(request, "pages/rules.html", context)


def loginPage(request):

    # delete message before load login page
    storage = messages.get_messages(request)
    for _ in storage:
        # Without this loop `_loaded_messages` is empty
        pass

    for _ in list(storage._loaded_messages):
        del storage._loaded_messages[0]

    if request.user.is_authenticated:
        return redirect("index")

    if request.method == "POST":
        username = request.POST.get("username").lower()
        password = request.POST.get("password")

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "User or password does not exist!")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            messages.error(request, "Please try again")

    context = {}
    return render(request, "pages/login.html", context)


def logoutUser(request):
    logout(request)
    return redirect("index")


def registerPage(request):
    # form = UserCreationForm()
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect("index")
        else:
            messages.error(request, form.errors.as_data)

    return render(request, "pages/register.html", {"form": form})


def ranking(request):
    user = User.objects.all().order_by("-points")
    paginator = Paginator(user, 10)
    page_num = request.GET.get("page")
    page_obj = paginator.get_page(page_num)
    context = {"users": user, "page_obj": page_obj}
    return render(request, "pages/ranking.html", context)


def userProfile(request, username):
    user = User.objects.get(username=username)
    context = {"user": user}
    return render(request, "pages/profile.html", context)


@login_required(login_url="login")
def problem_set(request):
    user = User.objects.all().order_by('-points')
    problem = Problem.objects.all().order_by('id')
    context = {'users': user, 'problems': problem}
    if request.GET.get('search')!= None:
        path = request.GET.get('search')
        if Problem.objects.filter(problemName = path).exists():        
            path_problem = Problem.objects.get(problemName=path)
            search = path_problem.id
            url = '/problem/' + str(search)
            return redirect(url)
        else:
            return redirect('/problem_set')
    return render(request, 'pages/problem_set.html', context)


@login_required(login_url="login")
def problemPage(request, id):
    problem = Problem.objects.filter(id=id)
    # context = {'problems': problem}

    # code editor
    codeareadata = ""
    lang = ""
    output = ""
    if request.method == "POST":
        codeareadata = request.POST["codearea"]
        lang = request.POST["languages"]
        try:
            if lang == "python":
                old_stdout = sys.stdout
                output = sys.stdout = StringIO()
                exec(codeareadata)
                sys.stdout = old_stdout
                output = output.getvalue()
            elif lang == "php":
                sys.stdout = open("file.php", "w")
                print(codeareadata)
                sys.stdout.close()

                output = os.popen("php file.php").read()

                # output = output.getvalue()
            elif lang == "javascript":
                sys.stdout = open("file.js", "w")
                print(codeareadata)
                sys.stdout.close()

                output = os.popen("node file.js").read()
            elif lang == "C++":
                sys.stdout = open("file.cpp", "w")
                print(codeareadata)
                sys.stdout.close()

                os.system("g++ file.cpp -o thisiscpp")
                output = os.popen("./thisiscpp").read()
            elif lang == "C":
                sys.stdout = open("file.c", "w")
                print(codeareadata)
                sys.stdout.close()

                os.system("gcc file.c -o thisisc")
                output = os.popen("./thisisc").read()
        except Exception as e:
            output = "Compile error!"

    return render(
        request,
        "pages/problem.html",
        {"problems": problem, "code": codeareadata, "output": output},
    )


@login_required(login_url="login")
def update_user(request):
    user = request.user
    form = UserForm(instance=user)
    if request.method == "POST":
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect("profile", username=user.username)

    return render(request, "pages/update_user.html", {"form": form})
