from django.shortcuts import render
from .models import Product

def product_list(request):
    """
    عرض قائمة المنتجات في المتجر
    """
    # 🛒 جلب جميع المنتجات من قاعدة البيانات
    products = Product.objects.all()

    # تمرير المنتجات إلى القالب
    context = {
        'products': products
    }

    # ✅ استخدام المسار الصحيح للقالب الذي أنشأته
    return render(request, 'products-templates/list.html', context)
