from django.urls import path
from .views import order

urlpatterns = [
    path('rezerwacje/', order, name='order')
]
