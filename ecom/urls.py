"""ecom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from accounts import urls as accounts_urls
from cart import urls as cart_urls
from category import urls as category_urls
from home import urls as home_urls
from order import urls as order_urls
from product import urls as product_urls
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include(accounts_urls)),
    path('cart/', include(cart_urls)),
    path('category/', include(category_urls)),
    path('', include(home_urls)),
    path('order/', include(order_urls)),
    path('product/', include(product_urls)),
]
urlpatterns += staticfiles_urlpatterns()
