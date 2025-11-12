# ==============================
# 🛒 /cart/urls.py
# ==============================
from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),                     # 🧾 عرض السلة
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart') # ➕ إضافة منتج للسلة
]
