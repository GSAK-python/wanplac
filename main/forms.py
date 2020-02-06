from django.forms import ModelForm
from .models import Terminy
from django import forms


class OrderForm(ModelForm):

    class Meta:
        model = Terminy.MyOrder
        fields = ['imie', 'nazwisko', 'email', 'data', 'godzina', 'trasa',
                  'traper', 'jett', 'finder', 'eoli', 'protour', 'family', 'koga', 'kanu', 'kod']
        help_texts = {
            'data': 'Maksymalna data rezerwacji wynosi 7 dni od dnia dzisiejszego.',
            'godzina': 'Możliwość rezerwacji kajaków obowiązuje w godzinach 9:00 - 12:00',
            'kod': 'Należy go podać w celu weryfikacji zamówienia podczas wydawania kajaków (w siedzibie firmy w Krutyni)',
            'email': 'Na adres email zostanie wysłane potwierdzenie rezerwacji.'
        }
        labels = {
            'imie': 'Imię',
            'protour': 'Pro-tour',
            'kod': 'Unikalny numer zamówienia',
        }
        widgets = {
            'kod': forms.TextInput(attrs={'readonly':'readonly'}),
            'stan': forms.TextInput(attrs={'readonly': 'readonly'})
        }
