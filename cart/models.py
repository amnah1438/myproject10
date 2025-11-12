# ==============================
# 🛒 /cart/admin.py
# ==============================
from django.contrib import admin
from .models import CartItem


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    """إدارة عناصر السلة من لوحة الأدمن"""

    # الأعمدة الظاهرة في القائمة
    list_display = ("product", "quantity", "session_key", "get_total_price_display")

    # خصائص الفلترة والبحث
    list_filter = ("product",)
    search_fields = ("product__name", "session_key")

    # ترتيب السجلات من الأحدث إلى الأقدم
    ordering = ("-id",)

    # الحقول المقروءة فقط
    readonly_fields = ("get_total_price_display",)

    # تقسيم الحقول في واجهة التحرير
    fieldsets = (
        ("🛍️ بيانات المنتج", {"fields": ("product", "quantity")}),
        ("💳 بيانات الجلسة", {"fields": ("session_key",)}),
        ("💰 المجموع الفرعي", {"fields": ("get_total_price_display",)}),
    )

    def get_total_price_display(self, obj):
        """عرض المجموع بصيغة مرتبة"""
        return f"{obj.get_total_price():,.2f} ريال"
    get_total_price_display.short_description = "المجموع الفرعي"
