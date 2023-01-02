from django.shortcuts import render, redirect
from django.contrib import messages
from cart.models import Cart, CartItem
from order.models import Order, OrderItem


# Create your views here.

def add(request):
    if request.method == "POST":
        user_id = request.user.id
        if not user_id:
            messages.error(request, 'Please login to continue')
            return redirect('accounts:login')
        cart_id = Cart.objects.get(user_id=user_id).id
        if not cart_id:
            messages.error(request, 'Cart items not found')
            return redirect('home:index')
        # get cart details
        get_cart = Cart.objects.select_related('address', 'shipping').filter(user_id=user_id).first()
        # create order
        c_order = Order(user_id=request.user.id, address_id=get_cart.address.id,
                        shipping_id=get_cart.shipping.id, shipping_method=get_cart.shipping_method,
                        discount=get_cart.discount, payment_type=request.POST.get('checkoutPaymentMethod'))
        c_order.save()
        order_id = c_order.id
        # get cart items
        items = CartItem.objects.select_related('product', 'cart').filter(cart_id=cart_id)
        total = 0
        if items:
            for temp in items:
                o_item = OrderItem(order_id=order_id, product_id=temp.product.id,
                                   quantity=temp.quantity)
                o_item.save()
                each = int(temp.quantity) * float(temp.product.price)
                total += each
        # update order again
        get_order = Order.objects.get(id=order_id)
        get_order.total = round(total, 2)
        get_order.save()
        clear_cart(request, cart_id, items)
        messages.success(request, "Order created successfully")
        return redirect("home:index")
    if request.method == "GET":
        return redirect('home:index')


def clear_cart(request, cart_id, items):
    cart_items = []
    for i in items:
        cart_items.append(i.id)
    for ids in cart_items:
        CartItem.objects.filter(id=ids).delete()
    Cart.objects.filter(id=cart_id).delete()
    return True
