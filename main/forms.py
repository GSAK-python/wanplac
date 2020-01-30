from django.forms import ModelForm
from .models import Order, MyOrder


class OrderForm(ModelForm):
    class Meta:
        model = MyOrder
        fields = ['imię', 'nazwisko', 'email', 'data', 'godzina', 'trasa', 'sprzęt']