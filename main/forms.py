from django.forms import ModelForm
from .models import MyOrder


class OrderForm(ModelForm):

    class Meta:
        model = MyOrder
        fields = ['imię', 'nazwisko', 'email', 'data', 'godzina', 'trasa',
                  'traper', 'jett', 'finder', 'eoli', 'protour', 'family', 'koga', 'kanu']
        help_texts = {
            'data': 'Maksymalna data rezerwacji wynosi 7 dni od dnia dzisiejszego.',
            'godzina': 'Możliwość rezerwacji kajaków obowiązuje w godzinach 9:00 - 12:00'
        }
        labels = {
            'protour': 'Pro-tour',
            'kod': 'Kod zamówienia'
        }
