from site import check_enableusersite
from django.db import models
#import numpy

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
    topping = models.CharField(max_length=255)

    def __str__(self):
        return self.topping

class Size(models.Model):
    size = models.CharField(max_length=255)

    def __str__(self):
        return self.size


class Cheese(models.Model):
    cheese = models.CharField(max_length=255)

    def __str__(self):
        return self.cheese
    
class Sauce(models.Model):
    sauce = models.CharField(max_length=255)

    def __str__(self):
        return self.sauce
    
class Crust(models.Model):
    crust = models.CharField(max_length=255)
    
    def __str__(self):
        return self.crust

def findValue(className, default):
    print(className.objects.filter())

class Pizza(models.Model):
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    cheese = models.ForeignKey(Cheese, on_delete=models.CASCADE)
    sauce = models.ForeignKey(Sauce, on_delete=models.CASCADE)
    crust = models.ForeignKey(Crust, on_delete=models.CASCADE)
    toppings = models.ManyToManyField(Topping, blank=True)

    def __str__(self):
        return F"Size: {self.size}, Cheese: {self.cheese}, Sauce: {self.sauce}, Crust: {self.crust}"

class Cart(models.Model):
    pizzas = models.ManyToManyField(Pizza, blank=True)
