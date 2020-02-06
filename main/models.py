from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from datetime import timedelta
from .templatetags.kod_generator import random_string


class Startowa(models.Model):
    obszar_nieedytowalny = models.CharField(max_length=128)

    def __str__(self):
        return self.obszar_nieedytowalny


class Terminy(models.Model):
    termin = models.DateField()

    class MyOrder(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        imie = models.CharField(max_length=128)
        nazwisko = models.CharField(max_length=128)
        email = models.EmailField()

        wybor_dat = {
            (0, dt.date.today().strftime('%d-%m-%Y')),
            (1, (dt.date.today() + timedelta(days=+1)).strftime('%d-%m-%Y')),
            (2, (dt.date.today() + timedelta(days=+2)).strftime('%d-%m-%Y')),
            (3, (dt.date.today() + timedelta(days=+3)).strftime('%d-%m-%Y')),
            (4, (dt.date.today() + timedelta(days=+4)).strftime('%d-%m-%Y')),
            (5, (dt.date.today() + timedelta(days=+5)).strftime('%d-%m-%Y')),
            (6, (dt.date.today() + timedelta(days=+6)).strftime('%d-%m-%Y'))
        }
        data = models.IntegerField(choices=sorted(wybor_dat))

        wybor_tras = {
            (0, 'Krutyń - Młyn (3km)'),
            (1, 'Krutyń - Rosocha (6km)'),
            (2, 'Krutyń - Ukta (13km)'),
            (3, 'Krutyń - Jezioro Mokre - Krutyń (10km)')
        }
        trasa = models.IntegerField(choices=sorted(wybor_tras))

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
        godzina = models.IntegerField(choices=sorted(wybor_godzin))

        traper_ilosc = {
            (0, '0'),
            (1, '1'),
            (2, '2'),
            (3, '3'),
            (4, '4')
        }
        traper = models.IntegerField(blank=True, default=0, choices=sorted(traper_ilosc))

        jett_ilosc = {
            (0, '0'),
            (1, '1'),
        }
        finder_ilosc = {
            (0, '0'),
            (1, '1'),
            (2, '2'),
            (3, '3'),
            (4, '4'),
            (5, '5'),
            (6, '6'),
            (7, '7'),
            (8, '8'),
            (9, '9'),
            (10, '10'),
            (11, '11'),
            (12, '12'),
            (13, '13'),
            (14, '14'),
            (15, '15'),
            (16, '16'),
            (17, '17'),
            (18, '18'),
            (19, '19'),
            (20, '20'),
            (21, '21'),
            (22, '22'),
            (23, '23'),
            (24, '24')
        }
        eoli_ilosc = {
            (0, '0'),
            (1, '1'),
            (2, '2'),
            (3, '3'),
            (4, '4'),
            (5, '5'),
            (6, '6'),
            (7, '7'),
            (8, '8'),
            (9, '9'),
            (10, '10')
        }
        protour_ilosc = {
            (0, '0'),
            (1, '1'),
            (2, '2'),
            (3, '3'),
            (4, '4'),
            (5, '5'),
            (6, '6'),
            (7, '7'),
            (8, '8')
        }
        family_ilosc = {
            (0, '0'),
            (1, '1'),
            (2, '2'),
            (3, '3'),
            (4, '4')
        }
        koga_ilosc = {
            (0, '0'),
            (1, '1'),
            (2, '2'),
            (3, '3')
        }
        kanu_ilosc = {
            (0, '0'),
            (1, '1'),
            (2, '2'),
            (3, '3')
        }

        jett = models.IntegerField(blank=True, default=0, choices=sorted(jett_ilosc))
        finder = models.IntegerField(blank=True, default=0, choices=sorted(finder_ilosc))
        eoli = models.IntegerField(blank=True, default=0, choices=sorted(eoli_ilosc))
        protour = models.IntegerField(blank=True, default=0, choices=sorted(protour_ilosc))
        family = models.IntegerField(blank=True, default=0, choices=sorted(family_ilosc))
        koga = models.IntegerField(blank=True, default=0, choices=sorted(koga_ilosc))
        kanu = models.IntegerField(blank=True, default=0, choices=sorted(kanu_ilosc))

        kod = models.CharField(max_length=6, default=random_string)

        def order_display(self):
            return 'Imię i nazwisko: {} {}'.format(self.imie, self.nazwisko)

        def __str__(self):
            return self.order_display()



