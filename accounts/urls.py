from django.urls import path, include
from accounts import views

app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('forgot_password', views.forgot_password, name="forgot_password"),
    path('test/', views.test, name='test')
]
