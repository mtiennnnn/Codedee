from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    username = models.CharField(unique=True, max_length=200, null=True)
    bio = models.TextField(null=False, default="Hello Codedee User", blank=True)
    avatar = models.ImageField(null=True, default="avatar.png", blank=False)