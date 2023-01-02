from django.urls import path, include
from order import views

app_name = "order"
urlpatterns = [
    # path('index/', views.login, name='cart_index'),
    path('complete/', views.add, name='complete'),

]
