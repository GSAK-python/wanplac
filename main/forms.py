from django.forms import ModelForm
from .models import MyOrder
from crispy_forms.bootstrap import InlineField


class OrderForm(ModelForm):
    class Meta:
        model = MyOrder
        fields = ['imię', 'nazwisko', 'email', 'data', 'godzina', 'trasa', 'sprzęt']
        help_texts = {
            'data': 'Maksymalna data rezerwacji wynosi 7 dni od dnia dzisiejszego.',
            'godzina': 'Możliwość rezerwacji kajaków obowiązuje w godzinach 9:00 - 12:00'
        }


class OrderForm2(ModelForm):

    class Meta:
        model = MyOrder
        fields = ['imię', 'nazwisko', 'email', 'data', 'godzina', 'trasa', 'sprzęt',
                  'traper', 'jett', 'finder', 'eoli', 'protour', 'family', 'koga', 'kanu']
        help_texts = {
            'data': 'Maksymalna data rezerwacji wynosi 7 dni od dnia dzisiejszego.',
            'godzina': 'Możliwość rezerwacji kajaków obowiązuje w godzinach 9:00 - 12:00'
        }
        labels = {
            'protour': 'Pro-tour'
        }