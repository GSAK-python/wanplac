from django.db import models


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

