from django.shortcuts import render, redirect, get_object_or_404
from .models import Order
from django.contrib.auth.decorators import login_required


@login_required
def order(request):
    rezerwacje = Order.objects.all()
    return render(request, 'rezerwacje.html', {'rezerwacje': rezerwacje})
