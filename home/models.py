from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Problem(models.Model):
    id = models.IntegerField(primary_key=True)
    problemName = models.CharField(unique=True, max_length=50, null=True)
    difficulty = models.CharField(null=True, max_length=15, blank=False)
    description = models.TextField(null=False, blank=False)
    short_des = models.TextField(null=True, blank=False)
    points = models.IntegerField(null=False, default=0, blank=False)
    icon = models.CharField(null=True, blank=False, max_length=30)
    testcase = models.TextField(null=False, blank=True)
    result = models.TextField(null=False, blank=True)
    #solved = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    def __str__(self):
        return self.problemName

class User(AbstractUser):
    username = models.CharField(unique=True, max_length=200, null=True)
    bio = models.TextField(null=False, default="Hello Codedee User", blank=True)
    avatar = models.ImageField(null=True, default="avatar.png", blank=False)
    points = models.IntegerField(null=False, default=100, blank=False)
    solved_chall = models.ManyToManyField(Problem, blank=True)