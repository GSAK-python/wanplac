from django.forms import ModelForm
from django import forms
from .models import MyOrder


class OrderForm(forms.ModelForm):
    class Meta:
        model = MyOrder
        fields = ['imię', 'nazwisko', 'email', 'data', 'godzina', 'trasa', 'sprzęt']
        help_texts = {
            'data': 'Maksymalna data rezerwacji wynosi 7 dni od dnia dzisiejszego.',
            'godzina': 'Możliwość rezerwacji kajaków obowiązuje w godzinach 9:00 - 12:00'
        }

"""
class KajakiForm(forms.Form):
    wybor_kajakow = {
        (0, 'Eoli'),
        (1, 'Finder'),
        (2, 'Traper'),
        (3, 'Jett')
    }
    n = forms.ChoiceField(label='Dostępne kajaki', choices=wybor_kajakow)
"""

