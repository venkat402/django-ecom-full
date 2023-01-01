from django.urls import path, include
from product import views

app_name = "product"
urlpatterns = [
    # path('index/', views.login, name='cart_index'),
    path('index/', views.product, name='index'),
]
