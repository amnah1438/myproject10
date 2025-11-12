from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product
from .models import CartItem

def cart_detail(request):
    session_key = request.session.session_key
    if not session_key:
        request.session.create()
    items = CartItem.objects.filter(session_key=request.session.session_key)
    total = sum(item.get_total_price() for item in items)
    return render(request, 'cart/cart_detail.html', {'items': items, 'total': total})

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    session_key = request.session.session_key
    if not session_key:
        request.session.create()
    cart_item, created = CartItem.objects.get_or_create(
        product=product,
        session_key=session_key,
    )
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart_detail')
