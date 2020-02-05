from django.urls import path
from .views import startowa, kajaki, trasy, signup, navbar, faq, nowe_zamowienie, potwierdzenie_zamowienia
from .views import my_order


urlpatterns = [
    path('startowa/', startowa, name='startowa'),
    path('kajaki/', kajaki, name='kajaki'),
    path('trasy/', trasy, name='trasy'),
    path('signup/', signup, name='signup'),
    path('navbar/', navbar, name='navbar'),
    path('faq/', faq, name='faq'),
    path('nowe_zamowienie/', nowe_zamowienie, name='nowe_zamowienie'),
    path('potwierdzenie_zamowienia/', potwierdzenie_zamowienia, name='potwierdzenie_zamowienia'),
    path('moje_rezerwacje/', my_order, name='my_order')
]
