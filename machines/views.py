from django.shortcuts import render, redirect
from .models import Machine


def machines(request):
    return render(request, 'machines/machines.html', {'machines': Machine.objects.all()})
