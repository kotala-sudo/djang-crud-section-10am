from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'website/home.html', {})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password = password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You were authenticated and logged in successfully.')
            return redirect('home')
        else:
            messages.success(request, 'Login failed, try again!')
            return redirect('login')
    else:
        return render(request, 'website/home.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('home')

