from django.shortcuts import render, redirect
from django.http import HttpResponse
from cart.models import Cart, CartItem
from django.contrib import messages
from product.models import Product
from address.models import Address


# Create your views here.

def index(request):
    user_id = request.user.id
    if not user_id:
        messages.error(request, 'Please login to continue')
        return redirect('accounts:login')
    cart_id = Cart.objects.get(user_id=user_id).id
    if not cart_id:
        result = {
            "items": [],
            "total": 0
        }
        return render(request, 'cart.html', context=result)
    items = CartItem.objects.select_related('product', 'cart').filter(cart_id=cart_id)
    total = 0
    if items:
        for temp in items:
            each = int(temp.quantity) * float(temp.product.price)
            temp.total = each
            total += each
    result = {
        "items": items,
        "total": round(total, 2)
    }
    return render(request, 'cart.html', context=result)


def add_cart(request):
    user_id = request.user.id
    if not user_id:
        messages.error(request, 'Please login to continue')
        return redirect('accounts:login')
    if request.method == "POST":
        product_id = request.POST.get('id')
        cart_id = Cart.objects.get(user_id=user_id).id
        if not cart_id:
            c = Cart(user_id=user_id)
            c.save()
            cart_id = c.id
        ci = CartItem.objects.filter(product_id=product_id, cart_id=cart_id).first()
        if ci:
            ci.quantity = int(ci.quantity) + 1
            ci.save()
            messages.error(request, 'Item already exist in cart')
            return redirect('cart:index')
        else:
            ci = CartItem(cart_id=cart_id, product_id=product_id, quantity=1)
            ci.save()
            messages.error(request, 'Item added to cart successfully')
            return redirect('cart:index')

    return render(request, 'cart.html')


def checkout_shipping(request):
    user_id = request.user.id
    if not user_id:
        messages.error(request, 'Please login to continue')
        return redirect('accounts:login')
    cart_id = Cart.objects.get(user_id=user_id).id
    if not cart_id:
        result = {
            "items": [],
            "total": 0
        }
        return render(request, 'checkout.html', context=result)
    items = CartItem.objects.select_related('product', 'cart').filter(cart_id=cart_id)
    total = 0
    if items:
        for temp in items:
            each = int(temp.quantity) * float(temp.product.price)
            temp.total = each
            total += each
    result = {
        "items": items,
        "total": round(total, 2)
    }
    return render(request, 'checkout-shipping.html', context=result)


def checkout_payment(request):
    return render(request, 'checkout-payment.html')


def checkout(request):
    user_id = request.user.id
    if not user_id:
        messages.error(request, 'Please login to continue')
        return redirect('accounts:login')
    cart_id = Cart.objects.get(user_id=user_id).id
    if not cart_id:
        result = {
            "items": [],
            "total": 0
        }
        return render(request, 'checkout.html', context=result)
    items = CartItem.objects.select_related('product', 'cart').filter(cart_id=cart_id)
    total = 0
    if items:
        for temp in items:
            each = int(temp.quantity) * float(temp.product.price)
            temp.total = each
            total += each
    result = {
        "items": items,
        "total": round(total, 2)
    }
    return render(request, 'checkout.html', context=result)


def save_address(request):
    user_id = request.user.id
    if request.method == "POST":
        billing = request.POST.get('billing')
        first_name = request.POST.get('s_first_name')
        last_name = request.POST.get('s_last_name')
        address = request.POST.get('s_address')
        state = request.POST.get('s_state')
        country = request.POST.get('s_country')
        zips = request.POST.get('s_zip')
        shipping = Address(user_id=request.user, type="shipping",
                           first_name=first_name, last_name=last_name,
                           address=address, state=state,
                           country=country, zip=zips)
        shipping.save()
        messages.success(request, "shipping address saved successfully")
        if billing:
            billing = Address(user_id=request.user, type="shipping",
                              first_name=first_name, last_name=last_name,
                              address=address, state=state,
                              country=country, zip=zip)
            billing.save()
            messages.success(request, "billing address saved successfully")
        else:
            first_name = request.POST.get('b_first_name')
            last_name = request.POST.get('b_last_name')
            address = request.POST.get('b_address')
            state = request.POST.get('b_state')
            country = request.POST.get('b_country')
            zips = request.POST.get('b_zip')
            billing = Address(user_id=request.user
                              , type="billing",
                              first_name=first_name, last_name=last_name,
                              address=address, state=state,
                              country=country, zip=zips)
            billing.save()
            messages.success(request, "billing address saved successfully")
        return redirect('cart:shipping')
    if request.method == "GET":
        return redirect('cart:shipping')
