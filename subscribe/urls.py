from django.urls import path, include
from subscribe import views

app_name = "subscribe"
urlpatterns = [
    # path('index/', views.login, name='cart_index'),
    path('', views.subscribe, name='index'),
]
