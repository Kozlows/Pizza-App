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

class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ['pizzas']

        