from django.shortcuts import render


# Create your views here.


def subscribe(request):
    return render(request, 'forgot_password.html')
