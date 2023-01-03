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
    cart_id = Cart.objects.filter(user_id=user_id).first()
    if not cart_id:
        result = {
            "items": [],
            "total": 0
        }
        return render(request, 'cart.html', context=result)
    cart_id = cart_id.id
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
        cart_id = Cart.objects.filter(user_id=user_id).first()
        if not cart_id:
            c = Cart(user_id=user_id)
            c.save()
            cart_id = c.id
        else:
            cart_id = cart_id.id
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
    cart_id = Cart.objects.filter(user_id=user_id).first()
    if not cart_id:
        result = {
            "items": [],
            "total": 0
        }
        return render(request, 'checkout.html', context=result)
    cart_id = cart_id.id
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
    user_id = request.user.id
    if not user_id:
        messages.error(request, 'Please login to continue')
        return redirect('accounts:login')
    cart_id = Cart.objects.filter(user_id=user_id).first()
    if not cart_id:
        result = {
            "items": [],
            "total": 0
        }
        return render(request, 'checkout.html', context=result)
    cart_id = cart_id.id
    items = CartItem.objects.select_related('product', 'cart').filter(cart_id=cart_id)
    total = 0
    cart = Cart.objects.select_related('address').get(id=cart_id)
    if items:
        for temp in items:
            each = int(temp.quantity) * float(temp.product.price)
            temp.total = each
            total += each
    result = {
        "items": items,
        "total": round(total, 2),
        "cart": cart
    }
    return render(request, 'checkout-payment.html', context=result)


def checkout(request):
    user_id = request.user.id
    if not user_id:
        messages.error(request, 'Please login to continue')
        return redirect('accounts:login')
    cart_id = Cart.objects.filter(user_id=user_id).first()
    if not cart_id:
        result = {
            "items": [],
            "total": 0
        }
        return render(request, 'checkout.html', context=result)
    cart_id = cart_id.id
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
        shipping_id = shipping.id
        messages.success(request, "shipping address saved successfully")
        if billing:
            billing = Address(user_id=request.user, type="shipping",
                              first_name=first_name, last_name=last_name,
                              address=address, state=state,
                              country=country, zip=zip)
            billing.save()
            billing_id = billing.id
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
            billing_id = billing.id
            messages.success(request, "billing address saved successfully")
        cart = Cart.objects.filter(user_id=user_id).first()
        cart.address_id = billing_id
        cart.shipping_id = shipping_id
        cart.save()
        return redirect('cart:shipping')
    if request.method == "GET":
        return redirect('cart:shipping')


def shipping_method(request):
    if request.method == "POST":
        user_id = request.user.id
        if not user_id:
            messages.error(request, 'Please login to continue')
            return redirect('accounts:login')
        cart_id = Cart.objects.filter(user_id=user_id).first()
        if not cart_id:
            result = {
                "items": [],
                "total": 0
            }
            return render(request, 'checkout-payment.html', context=result)
        cart_id = cart_id.id
        data = Cart.objects.filter(id=cart_id).first()
        data.shipping_method = request.POST.get('checkoutShippingMethod')
        data.save()
        messages.success(request, "shipping method saved successfully")
        return redirect('cart:payment')
    if request.method == "GET":
        return redirect('cart:payment')
