# ==============================
# 🧱 /cart/models.py
# ==============================
from django.db import models
from products.models import Product


class CartItem(models.Model):
    """🛒 نموذج يمثل عنصر داخل سلة المشتريات"""

    # 🔗 المنتج المرتبط بالسلة
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name="المنتج"
    )

    # 🔢 الكمية المضافة
    quantity = models.PositiveIntegerField(
        default=1,
        verbose_name="الكمية"
    )

    # 🧩 مفتاح الجلسة لتمييز المستخدم قبل تسجيل الدخول
    session_key = models.CharField(
        max_length=255,
        verbose_name="مفتاح الجلسة"
    )

    # 🕒 وقت الإضافة (اختياري لكنه مفيد في الأدمن)
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاريخ الإضافة"
    )

    class Meta:
        verbose_name = "عنصر سلة"
        verbose_name_plural = "عناصر السلة"
        ordering = ["-created_at"]

    def __str__(self):
        """عرض جميل لاسم المنتج والكمية"""
        return f"{self.product.name} × {self.quantity}"

    def get_total_price(self):
        """💰 حساب المجموع الفرعي لهذا العنصر"""
        return self.product.price * self.quantity
