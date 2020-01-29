from django.forms import ModelForm
from .models import Order


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['imię', 'nazwisko', 'email', 'data', 'godzina', 'trasa', 'sprzęt']