from django.shortcuts import render, redirect, get_object_or_404
from .models import Order, Startowa
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
# from django.contrib.auth.hashers import make_password


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
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})



