from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *

def gologin(request):
    return redirect('login')

def login(request):
    user = get_object_or_404(User, id=idk)
    if request.method == "POST":
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserForm(instance=user)
    return render(request, 'index.html', {"form": form})

def signup(request):
    return render(request, 'accountCreation.html')

def home(request):
    return render(request, 'home.html')

def selection(request):
    return render(request, 'pizzaSelection.html')

def cart(request):
    return render(request, 'cart.html')

def payment(request):
    return render(request, 'payment.html')


