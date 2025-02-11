from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import Login

def gologin(request):
    return redirect('login')

def login(request):
    return render(request, 'index.html')

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