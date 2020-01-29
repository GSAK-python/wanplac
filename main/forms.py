from django.forms import ModelForm
from .models import Order, MyOrder


class OrderForm(ModelForm):
    class Meta:
        model = Order
        model = MyOrder
        fields = ['imię', 'nazwisko', 'email', 'data', 'godzina', 'trasa', 'sprzęt']