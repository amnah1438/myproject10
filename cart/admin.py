# ==============================
# 🛒 /Users/amnah/myproject10/cart/admin.py
# ==============================
from django.contrib import admin
from .models import CartItem


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ("product", "quantity", "session_key", "created_at")
    list_filter = ("created_at",)
    search_fields = ("product__name", "session_key")
    ordering = ("-created_at",)

    # 🧾 طريقة عرض أجمل داخل لوحة الأدمن
    fieldsets = (
        ("معلومات المنتج", {"fields": ("product", "quantity")}),
        ("معلومات الجلسة", {"fields": ("session_key",)}),
        ("البيانات الزمنية", {"fields": ("created_at",)}),
    )

    readonly_fields = ("created_at",)
