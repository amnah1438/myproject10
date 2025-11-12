# ==============================
# 🛒 /cart/views.py
# ==============================
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from products.models import Product
from .models import CartItem


# ==============================
# 🛍️ عرض تفاصيل السلة
# ==============================
def cart_detail(request):
    # التأكد من وجود جلسة للمستخدم
    session_key = request.session.session_key
    if not session_key:
        request.session.create()

    # استرجاع العناصر من السلة الخاصة بهذه الجلسة
    items = CartItem.objects.filter(session_key=session_key)
    total = sum(item.get_total_price() for item in items)

    # تمرير البيانات إلى القالب
    context = {
        'items': items,
        'total': total,
    }
    return render(request, 'cart-templates/cart_detail.html', context)


# ==============================
# ➕ إضافة منتج إلى السلة
# ==============================
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
        messages.info(request, f"تم زيادة الكمية من المنتج: {product.name}")
    else:
        messages.success(request, f"✅ تمت إضافة {product.name} إلى السلة بنجاح!")

    return redirect('cart_detail')
