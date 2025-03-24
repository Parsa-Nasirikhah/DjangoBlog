from django.shortcuts import render
from .forms import Register
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate,logout

def register(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/post/home')
    else:
        if request.method == 'POST':
            form = Register(request.POST)
            if form.is_valid():
                form.save()
                homeurl = reverse('home')
                return HttpResponseRedirect(homeurl)
        else:
            form = Register()
        return render(request, 'register.html', {'form' : form})

def auth_login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/post/home')
    else:
        if request.method == 'POST':
            form = AuthenticationForm(request = request, data = request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username = username, password = password)
                if user is not None:
                    login(request, user)
                    homeurl = reverse('home')
                    return HttpResponseRedirect(homeurl)
        else:
            form = AuthenticationForm()
        return render(request, 'login.html', {'form' : form})
    
def auth_logout(request):
    logout(request)
    return HttpResponseRedirect('/accounts/signin')