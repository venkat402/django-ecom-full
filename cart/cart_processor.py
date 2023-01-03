from django.contrib import messages
from cart.models import Cart, CartItem


def get_cart(request):
    user_id = request.user.id
    if not user_id:
        result = {"cart": {
            "items": [],
            "total": 0
        }}
        return result
    cart_id = Cart.objects.filter(user_id=user_id).first()
    if not cart_id:
        result = {"cart": {
            "cart_items": [],
            "total": 0
        }}
        return result
    cart_id = cart_id.id
    items = CartItem.objects.select_related('product', 'cart').filter(cart_id=cart_id)
    total = 0
    if items:
        for temp in items:
            each = int(temp.quantity) * float(temp.product.price)
            temp.total = each
            total += each
    result = {"cart": {
        "items": items,
        "total": round(total, 2)
    }}
    return result
