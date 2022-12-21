from django import forms 
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.forms import ModelForm

class RegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'type':'text',
            'name':'username',
            'required':'required',
            'placeholder':'Choose a fabulous username',
        })
        self.fields['password1'].widget.attrs.update({
            'type':'password',
            'name':'password1',
            'required':'required',
            'placeholder':'Choose a password',
        })
        self.fields['password2'].widget.attrs.update({
            'type':'password',
            'name':'password2',
            'required':'required',
            'placeholder':'Confirm password',
        })
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['bio', 'avatar']