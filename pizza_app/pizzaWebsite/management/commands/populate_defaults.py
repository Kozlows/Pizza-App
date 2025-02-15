from django.core.management.base import BaseCommand
from pizzaWebsite.models import *

class Command(BaseCommand):
    help = "Populates the database with default pizza options"

    def handle(self, *args, **kwargs):
        sizes = "Small,Medium,Large".split(",")
        cheeses = "Mozzarella,Vegan,Low fat".split(",")
        sauces = "Tomato,BBQ".split(",")
        crusts = "Normal,Thin,Thick,Gluten Free".split(",")
        toppings = "Pepperoni,Chicken,Ham,Pineapple,Peppers,Mushrooms,Onions".split(",")

        classes = [Size, Cheese, Sauce, Crust, Topping]
        options = [sizes, cheeses, sauces, crusts, toppings]

        data = {className : option for className, option in zip(classes, options)}

        for i, items in enumerate(data.items()):
            model, options = items
            for option in options:
                if model is Size:
                    obj, created = model.objects.get_or_create(size = option)
                elif model is Cheese:
                    obj, created = model.objects.get_or_create(cheese = option)
                elif model is Sauce:
                    obj, created = model.objects.get_or_create(sauce = option)
                elif model is Crust:
                    obj, created = model.objects.get_or_create(crust = option)
                elif model is Topping:
                    obj, created = model.objects.get_or_create(topping = option)
                status = "Created" if created else "Already exists"
                self.stdout.write(f"{status}: {obj}")

        self.stdout.write(self.style.SUCCESS("Default pizza options populated successfully!"))