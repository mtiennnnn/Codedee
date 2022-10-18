from django.urls import path, include
from . import views
import sys
sys.setrecursionlimit(10000)

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('rules/', views.rules, name='rules'),
    path('login/', views.loginPage, name='login'),
    path('register/', views.register, name='register'),
    path('ranking/', views.ranking, name='ranking'),
    path('problem_set/', views.problem_set, name='problem_set'),
]
