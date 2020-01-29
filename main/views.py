from django.shortcuts import render, redirect, get_object_or_404
from .models import Order, Startowa, MyOrder
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from .forms import OrderForm


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


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('startowa')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def navbar(request):
    return render(request, 'navbar.html')


def faq(request):
    return render(request, 'faq.html')


@login_required
def nowe_zamowienie(request):
    zamowienie = OrderForm(request.POST or None, request.FILES or None)

    if zamowienie.is_valid():
        zamowienie.save()
        return redirect(potwierdzenie_zamowienia)

    return render(request, 'formularz_rezerwacji.html', {'zamowienie': zamowienie})


@login_required
def my_order(request):
    moje_zamowienie = MyOrder.objects.all()
    return render(request, 'moje_rezerwacje.html', {'moje_zamowienie': moje_zamowienie})


def potwierdzenie_zamowienia(request):
    return render(request, 'potwierdzenie_zamowienia.html')
