from django.urls import path
from .views import order, startowa, kajaki, trasy

urlpatterns = [
    path('rezerwacje/', order, name='order'),
    path('startowa/', startowa, name='startowa'),
    path('kajaki/', kajaki, name='kajaki'),
    path('trasy/', trasy, name='trasy')
]
