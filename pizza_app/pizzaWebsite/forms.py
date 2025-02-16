from django import forms
from .models import *

class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ['size', 'cheese', 'crust', 'toppings', 'sauce']

    toppings = forms.ModelMultipleChoiceField(
        queryset = Topping.objects.all(),
        widget = forms.CheckboxSelectMultiple,
        required = False
    )

    def save(self):
        pizza = super().save()
        pizza.updatePrice()
        return pizza


'''
1. Complete Cart, aka make use of its form, and add features to add/remove to specific quantities of pizza, delete pizzas althogether, or edit them.
1.1. Also add buttons to either go to payment or to make another pizza
2. Make it so you can make the cart an order, empting the cart in the process, and showing the order on home page
3. Making the payment page, where you have to input your card details to actually pay for the order.
4. Setting up admin page as requested
5. Work on the front-end to make it more original
6. Make a video of it

'''

