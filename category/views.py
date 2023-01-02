from django.shortcuts import render
from category.models import Category
from product.models import Product
from django.http import JsonResponse, HttpResponse


# Create your views here.

def category(request):
    return render(request, 'category.html')


def page(request, cat_id):
    cat = Category.objects.get(id=cat_id)
    products = Product.objects.filter(category_id=cat_id)
    result = {
        "category": cat,
        "products": products,
    }
    return render(request, 'category2.html', context=result)
