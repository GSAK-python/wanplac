from django.db import models
from django.contrib.auth.models import User


class Order(models.Model):
    imię = models.CharField(max_length=128)
    nazwisko = models.CharField(max_length=128)
    data = models.DateField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    godzina = models.TimeField(null=True, blank=True)
    trasa = models.TextField(default='')
    sprzęt = models.TextField(default='')

    def order_display(self):
        return 'Zamówienie: {} {}'.format(self.imię, self.nazwisko)

    def __str__(self):
        return self.order_display()


class Startowa(models.Model):
    obszar_nieedytowalny = models.CharField(max_length=128)

    def __str__(self):
        return self.obszar_nieedytowalny



