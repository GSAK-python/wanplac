from django.urls import path
from .views import order, startowa

urlpatterns = [
    path('rezerwacje/', order, name='order'),
    path('startowa/', startowa, name='startowa')
]
