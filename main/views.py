from django.shortcuts import render, redirect, get_object_or_404
from .models import Order, Startowa
from django.contrib.auth.decorators import login_required


@login_required
def order(request):
    rezerwacje = Order.objects.all()
    return render(request, 'rezerwacje.html', {'rezerwacje': rezerwacje})


def startowa(request):
    pozycje = Startowa.objects.all()
    return render(request, 'startowa.html', {'pozycje': pozycje})


def kajaki(request):
    return render(request, 'kajaki.html')


def trasy(request):
    return render(request, 'trasy.html')


