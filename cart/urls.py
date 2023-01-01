from django.urls import path, include
from cart import views

app_name = "cart"
urlpatterns = [
    path('index/', views.index, name='index'),
    path('shipping/', views.checkout_shipping, name="shipping"),
    path('payment/', views.checkout_payment, name="payment"),
    path('checkout/', views.checkout, name="checkout"),
]
