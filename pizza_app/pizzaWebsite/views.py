from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as authLogin, logout as authLogout
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

def gologin(request):
    return redirect('login')

@login_required(login_url='/login/')
def signout(request):
    authLogout(request)
    return redirect('login')

def login(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            authLogin(request, form.get_user())
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {"form" : form})

def signup(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            authLogin(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {"form" : form})

@login_required(login_url='/login/')
def home(request):
    return render(request, 'home.html')

@login_required(login_url='/login/')
def selection(request):
    if request.method == "POST":
        form = PizzaForm(request.POST)
        if form.is_valid():
            pizza = form.save()
            userCart = Cart.objects.get(user=request.user)
            otherPizzaID = userCart.hasPizza(pizza)
            if not otherPizzaID:
                userCart.pizzas.add(pizza)
            else:
                userCart.pizzas.get(id=otherPizzaID).addExtra()
            userCart.updatePrice()
            return redirect('cart')
    else:
        form = PizzaForm()
    return render(request, 'pizzaSelection.html', {"form" : form})

@login_required(login_url='/login/')
def cart(request):
    userCart = Cart.objects.get(user=request.user)
    pizzas = userCart.pizzas.all()
    return render(request, 'cart.html', {"pizzas": pizzas, "cart" : userCart})

@login_required(login_url='/login/')
def payment(request):
    return render(request, 'payment.html')


