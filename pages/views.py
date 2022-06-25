from django.shortcuts import render, redirect
from accounts.forms import LoginForm

def index(request):
    if request.user.is_authenticated: 
        return redirect('dashboard')
    else:
        return redirect('login')