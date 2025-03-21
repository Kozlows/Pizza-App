from site import check_enableusersite
from django.db import models
from django.contrib.auth.models import User
from django.core import validators
from datetime import datetime, timedelta

# Create your models here.
# EVERY TIME YOU MODIFY THIS FILE YOU HAVE TO MIGRATE YOUR DATABASE
# run these two commans 
# python manage.py makemigrations
# python manage.py migrate

# To add variables to the database of a specific class:
# python manage.py shell
# from {yourapp}.models import *
# 
# View all: {className}.objects.all()
# ex. Size.objects.all()
# Add one: {className}.objects.create({variableName0}=value0, {variableName1}=value1)
# ex. Size.objects.create(size="Extra Large", price=15.00)
# Delete one: {className}.objects.filter({variableName0}=value0).delete()
# ex. Size.objects.filter(size="Extra Large").delete()

    
class Topping(models.Model):
    part = models.CharField(max_length=255)
    price = models.FloatField()

    def __str__(self):
        return self.part

class Size(models.Model):
    part = models.CharField(max_length=255)
    price = models.FloatField()

    def __str__(self):
        return self.part


class Cheese(models.Model):
    part = models.CharField(max_length=255)
    price = models.FloatField()

    def __str__(self):
        return self.part
    
class Sauce(models.Model):
    part = models.CharField(max_length=255)
    price = models.FloatField()

    def __str__(self):
        return self.part
    
class Crust(models.Model):
    part = models.CharField(max_length=255)
    price = models.FloatField()
    
    def __str__(self):
        return self.part

class Pizza(models.Model):
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    cheese = models.ForeignKey(Cheese, on_delete=models.CASCADE)
    sauce = models.ForeignKey(Sauce, on_delete=models.CASCADE)
    crust = models.ForeignKey(Crust, on_delete=models.CASCADE)
    toppings = models.ManyToManyField(Topping, blank=True)
    price = models.FloatField(default=0.0)
    quantity = models.IntegerField(default=1)
    total = models.FloatField(default=0.0)

    def updatePrice(self):
        basePrice = sum((self.size.price, self.cheese.price, self.sauce.price, self.crust.price))
        self.price = basePrice + sum(topping.price for topping in self.toppings.all())
        self.updateTotal()
        self.save()

    def updateTotal(self):
        self.total = self.price * self.quantity

    def minusExtra(self):
        self.quantity -= 1
        if self.quantity <= 0:
            self.delete()
        self.updateTotal()
        self.save()

    def addExtra(self):
        self.quantity += 1
        self.updateTotal()
        self.save()

    def __str__(self):
        s = f"<{', '.join([f"{topping}" for topping in self.toppings.all()])}>"
        return f"Size: {self.size}, Cheese: {self.cheese}, Sauce: {self.sauce}, Crust: {self.crust}, {s}"

class Payment(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField()
    card = models.CharField(max_length=16)
    expiryMonth = models.IntegerField(default=1, validators=[validators.MinValueValidator(1), validators.MaxValueValidator(12)])
    expiryYear = models.IntegerField(default=1, validators=[validators.MinValueValidator(datetime.today().year % 100), validators.MaxValueValidator((datetime.today().year + 10) % 100)])
    cvv = models.CharField(max_length=3)

class Order(models.Model):
    pizzas = models.ManyToManyField(Pizza, blank=True)
    ordered_at = models.DateTimeField(auto_now_add=True)
    due = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        s = " --- ".join([f"{pizza}" for pizza in self.pizzas.all()])
        return s

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pizzas = models.ManyToManyField(Pizza, blank=True)
    price = models.FloatField(default=0.0)
    paymentInfo = models.OneToOneField(Payment, null=True, blank=True, on_delete=models.CASCADE)
    orders = models.ManyToManyField(Order, blank=True)

    def updatePrice(self):
        price = sum(pizza.total for pizza in self.pizzas.all())
        self.price = price
        self.save()

    def hasPizza(self, pizza):
        for cartPizza in self.pizzas.all():
            if cartPizza.size == pizza.size and cartPizza.cheese == pizza.cheese and cartPizza.sauce == pizza.sauce and cartPizza.crust == pizza.crust:
                if set(cartPizza.toppings.all()) == set(pizza.toppings.all()):    
                    return cartPizza.id
        return None
    
    def clear_cart(self):
        self.pizzas.clear()
