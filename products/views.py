from django.shortcuts import render
from .models import Product

def product_list(request):
    """
    عرض قائمة المنتجات في المتجر
    """
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'products/list.html', context)
