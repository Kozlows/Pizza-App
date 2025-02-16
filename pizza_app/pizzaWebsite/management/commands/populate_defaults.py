from django.core.management.base import BaseCommand
from pizzaWebsite.models import *

class Command(BaseCommand):
    help = "Populates the database with default pizza options"

    def handle(self, *args, **kwargs):
        sizes = [(part, price) for part, price in zip("Small,Medium,Large".split(","), [4.0, 5.5, 6.8])]
        cheeses = [(part, price) for part, price in zip("Mozzarella,Vegan,Low fat".split(","), [2.2, 3.6, 2.8])]
        sauces = [(part, price) for part, price in zip("Tomato,BBQ".split(","), [0.35, 0.50])]
        crusts = [(part, price) for part, price in zip("Normal,Thin,Thick,Gluten Free".split(","), [2.4, 1.8, 3.15, 3.0])]
        toppings = [(part, price) for part, price in zip("Pepperoni,Chicken,Ham,Pineapple,Peppers,Mushrooms,Onions".split(","), [0.65, 0.75, 0.4, 2.0, 0.4, 0.35, 0.25])]

        classes = [Size, Cheese, Sauce, Crust, Topping]
        options = [sizes, cheeses, sauces, crusts, toppings]

        data = {className : option for className, option in zip(classes, options)}

        for model, options in data.items():
            for part, price in options:
                obj, created = model.objects.get_or_create(part = part, price = price)
                
                status = "Created" if created else "Already exists"
                self.stdout.write(f"{status}: {obj}")

        self.stdout.write(self.style.SUCCESS("Default pizza options populated successfully!"))