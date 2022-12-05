from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
import sys
sys.setrecursionlimit(10000)

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('rules/', views.rules, name='rules'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerPage, name='register'),
    path('ranking/', views.ranking, name='ranking'),
    path('problem_set/', views.problem_set, name='problem_set'),
    path('profile/<str:username>/', views.userProfile, name='profile'),
    path('setting/', views.update_user, name='setting'),
    path('problem/<str:id>/', views.problemPage, name='problem'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)