from django.shortcuts import render
from product.models import Product
from django.http import JsonResponse, HttpResponse
from django.forms.models import model_to_dict
from django.core import serializers
from django.db.models import Q


# Create your views here.

def product(request):
    return render(request, 'product.html')


import json


def product_details(request, product_id):
    details = Product.objects.get(id=product_id)
    cat_id = details.category_id
    related = Product.objects.filter(category_id=cat_id)
    result = {
        "data": details,
        "related": related
    }
    return render(request, 'product.html', context=result)


def search_product(request):
    search = request.GET.get('name')
    products = Product.objects.filter(Q(name__icontains=search) | Q(description__icontains=search))
    result = {
        "search": search,
        "products": products,
    }

    return render(request, 'search.html', context=result)
