from django.urls import path, include
from category import views

app_name = "category"

urlpatterns = [
    # path('index/', views.login, name='cart_index'),
    path('index/', views.category, name="index"),
    path('<int:cat_id>', views.page, name='details')
]
