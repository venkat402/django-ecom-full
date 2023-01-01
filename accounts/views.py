from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


def test(request):
    return HttpResponse("Hello venkatesh")


def forgot_password(request):
    return render(request, 'forgotten-password.html')
