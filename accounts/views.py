from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth


# Create your views here.


def register(request):
    if request.method == "POST":
        try:
            User.objects.get(email=request.POST['email'])
            exist = True
            return render(request, 'register.html', {'error': 'Username is already taken!'})
        except User.DoesNotExist:
            exist = False
        if not exist:
            user = User.objects.create_user(request.POST['first_name'], request.POST['last_name'],
                                            request.POST['email'], password=request.POST['password'])
            auth.login(request, user)
            return redirect('home:index')
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email, password)
        if user:
            auth.login(request, user)
        else:
            return render(request, 'login.html', {'error': 'Username or password is incorrect!'})
    else:
        return render(request, 'login.html')


def test(request):
    return HttpResponse("Hello venkatesh")


def logout(request):
    auth.logout(request)
    return redirect("home:index")


def forgot_password(request):
    return render(request, 'forgotten-password.html')
