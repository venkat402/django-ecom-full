from django.urls import path, include
from address import views

app_name = "address"
urlpatterns = [
    path('index/', views.index, name='index'),
]
