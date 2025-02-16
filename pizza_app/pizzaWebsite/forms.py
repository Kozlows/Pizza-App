from django import forms
from django.core import validators
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

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['name', 'address', 'card', 'expiryMonth', 'expiryYear', 'cvv']

        widgets = {
            'card': forms.TextInput(attrs={'pattern': '[0-9]{16}', 'title': '16 digits required', 'inputmode': 'numeric', 'max_length': 16}),
            'cvv': forms.TextInput(attrs={'pattern': '[0-9]{3}', 'title': '3 digits required', 'inputmode': 'numeric', 'max_length': 3}),
        }

'''
2. Make it so you can make the cart an order, empting the cart in the process, and showing the order on home page
3. Making the payment page, where you have to input your card details to actually pay for the order.
4. Setting up admin page as requested
5. Work on the front-end to make it more original
6. Make a video of it

'''

