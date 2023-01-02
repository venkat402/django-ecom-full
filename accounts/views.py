from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.contrib import auth
from django.contrib import messages

User = get_user_model()


# Create your views here.


def register(request):
    User = get_user_model()
    if request.method == "POST":
        exist = None
        try:
            User.objects.get(email=request.POST['email'])
            exist = True
        except User.DoesNotExist:
            exist = False
        if exist:
            messages.error(request, 'User email already exists')
            return render(request, 'register.html')
        else:
            user = User.objects.create_user(username=request.POST.get('email'),
                                            first_name=request.POST.get('first_name'),
                                            last_name=request.POST.get('last_name'),
                                            email=request.POST.get('email'),
                                            password=request.POST.get('password'))
            auth.login(request, user)
            messages.success(request, 'welcome come back!')
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
