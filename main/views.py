from django.shortcuts import render, redirect, get_object_or_404
from .models import Order


# Create your views here.

def order(request):
    rezerwacje = Order.objects.all()
    return render(request, 'rezerwacje.html', {'rezerwacje': rezerwacje})