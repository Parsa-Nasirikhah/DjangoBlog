from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class Register(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        