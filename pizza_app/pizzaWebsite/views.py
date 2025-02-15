from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import *

def gologin(request):
    return redirect('login')

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'accountCreation.html')

def home(request):
    return render(request, 'home.html')

def selection(request):
    if request.method == "POST":
        form = PizzaForm(request.POST)
        if form.is_valid():
            print("Validaf")
            form.save()
            return redirect('cart')
        else:
            print("Not Valid")
    else:
        form = PizzaForm()
        print("Not POST")
    return render(request, 'pizzaSelection.html', {"form" : form})

def cart(request):
    form = CartForm()
    print(form)
    return render(request, 'cart.html', {"form": form})

def payment(request):
    return render(request, 'payment.html')


