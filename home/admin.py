from django.contrib import admin

from .models import User, Problem

admin.site.register(User)
admin.site.register(Problem)
# Register your models here.