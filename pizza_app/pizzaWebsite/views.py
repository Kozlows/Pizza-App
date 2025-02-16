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
    userCart = Cart.objects.get(user=request.user)
    orders = userCart.orders.all()
    for order in orders:
        order.due = order.ordered_at + timedelta(hours=2)
        if order.due <= datetime.now(order.due.tzinfo):  # AKA it has been delivered
            order.delete()

    return render(request, 'home.html', {"orders" : orders})

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
    userCart = Cart.objects.get(user=request.user)
    if request.method == "POST":
        form = PaymentForm(request.POST)
        
        if form.is_valid():
            paymentInfo = form.save()
            userCart.paymentInfo = paymentInfo
            userCart.save()
            return redirect('confirm')

    if userCart.paymentInfo != None:
        form = PaymentForm(instance=userCart.paymentInfo)
    else:
        form = PaymentForm()
    print(userCart.paymentInfo != None)
    return render(request, 'payment.html', {"form" : form})

@login_required(login_url='/login/')
def confirmation(request):
    userCart = Cart.objects.get(user=request.user)
    if request.method == "POST":
        new_order = Order.objects.create()
        
        # Copy all pizzas from the cart into the new order
        new_order.pizzas.set(userCart.pizzas.all())
        
        # Add the new order to the user's cart
        userCart.orders.add(new_order)

        userCart.clear_cart()
        userCart.save()
        return redirect("home")

    return render(request, 'completeOrder.html', {"info" : userCart.paymentInfo, "cart" : userCart, "pizzas" : userCart.pizzas.all()})



@login_required(login_url='/login/')
def increase(request, pizzaID):
    if request.method == "POST":
        userCart = Cart.objects.get(user=request.user)
        pizza = userCart.pizzas.get(id=pizzaID)
        pizza.addExtra()
        userCart.updatePrice()
    return redirect('cart')

@login_required(login_url='/login/')
def decrease(request, pizzaID):
    if request.method == "POST":
        userCart = Cart.objects.get(user=request.user)
        pizza = userCart.pizzas.get(id=pizzaID)
        pizza.minusExtra()
        userCart.updatePrice()
    return redirect('cart')



@login_required(login_url='/login/')
def delete(request, pizzaID):
    if request.method == "POST":
        userCart = Cart.objects.get(user=request.user)
        pizza = userCart.pizzas.get(id=pizzaID)
        pizza.delete()
        userCart.updatePrice()
    return redirect('cart')