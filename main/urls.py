from django.urls import path
from .views import order, startowa, kajaki, trasy, signup, navbar, faq

urlpatterns = [
    path('rezerwacje/', order, name='order'),
    path('startowa/', startowa, name='startowa'),
    path('kajaki/', kajaki, name='kajaki'),
    path('trasy/', trasy, name='trasy'),
    path('signup/', signup, name='signup'),
    path('navbar/', navbar, name='navbar'),
    path('faq/', faq, name='faq')

]
