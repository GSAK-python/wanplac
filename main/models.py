from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from datetime import timedelta
from django import forms


class Startowa(models.Model):
    obszar_nieedytowalny = models.CharField(max_length=128)

    def __str__(self):
        return self.obszar_nieedytowalny


class MyOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imię = models.CharField(max_length=128)
    nazwisko = models.CharField(max_length=128)
    email = models.EmailField()
    sprzęt = models.IntegerField()

    wybor_dat = {
        (0, dt.date.today().strftime('%d-%m-%Y')),
        (1, (dt.date.today() + timedelta(days=+1)).strftime('%d-%m-%Y')),
        (2, (dt.date.today() + timedelta(days=+2)).strftime('%d-%m-%Y')),
        (3, (dt.date.today() + timedelta(days=+3)).strftime('%d-%m-%Y')),
        (4, (dt.date.today() + timedelta(days=+4)).strftime('%d-%m-%Y')),
        (5, (dt.date.today() + timedelta(days=+5)).strftime('%d-%m-%Y')),
        (6, (dt.date.today() + timedelta(days=+6)).strftime('%d-%m-%Y'))
    }
    wybor_dat_posortowany = sorted(wybor_dat)
    data = models.IntegerField(choices=wybor_dat_posortowany)

    wybor_tras = {
        (0, 'Krutyń - Młyn (3km)'),
        (1, 'Krutyń - Rosocha (6km)'),
        (2, 'Krutyń - Ukta (13km)'),
        (3, 'Krutyń - Jezioro Mokre - Krutyń (10km)')
    }
    wobor_tras_posortowany = sorted(wybor_tras)
    trasa = models.IntegerField(choices=wobor_tras_posortowany)

    wybor_godzin = {
        (0, '9:00'),
        (1, '9:15'),
        (2, '9:30'),
        (3, '9:45'),
        (4, '10:00'),
        (5, '10:15'),
        (5, '10:30'),
        (7, '10:45'),
        (8, '11:00'),
        (9, '11:15'),
        (10, '11:30'),
        (11, '11:45'),
        (12, '12:00')
    }
    wybor_godzin_posortowany = sorted(wybor_godzin)
    godzina = models.IntegerField(choices=wybor_godzin_posortowany)

    def order_display(self):
        return 'Zamówienie: {} {}'.format(self.imię, self.nazwisko)

    def __str__(self):
        return self.order_display()


