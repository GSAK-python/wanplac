from django.forms import ModelForm
from django import forms
from .models import MyOrder


class OrderForm(forms.ModelForm):
    class Meta:
        model = MyOrder
        fields = ['imię',  'nazwisko', 'email', 'data', 'godzina', 'trasa', 'sprzęt']
        help_texts = {
            'data': 'Maksymalna data rezerwacji wynosi 7 dni od dnia dzisiejszego.',
            'godzina': 'Możliwość rezerwacji kajaków obowiązuje w godzinach 9:00 - 12:00'
        }
