from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return render(request, 'cart.html')


def checkout_shipping(request):
    return render(request, 'checkout-shipping.html')


def checkout_payment(request):
    return render(request, 'checkout-payment.html')


def checkout(request):
    return render(request, 'checkout.html')
