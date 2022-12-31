from django.urls import path, include
from accounts import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('test/', views.test, name='test')
]
