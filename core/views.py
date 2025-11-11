from django.shortcuts import render
from products.models import Product  # ✅ استدعاء الموديل من تطبيق المنتجات

def home(request):
    """
    الصفحة الرئيسية تعرض المنتجات من قاعدة البيانات
    """
    products = Product.objects.all()  # 🛒 جلب المنتجات من قاعدة البيانات
    context = {'products': products}
    return render(request, 'products-templates/list.html', context)
