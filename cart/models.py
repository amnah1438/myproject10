# ==============================
# 🧱 /cart/models.py
# ==============================
from django.db import models
from products.models import Product


class CartItem(models.Model):
    """نموذج عنصر السلة"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="المنتج")
    quantity = models.PositiveIntegerField(default=1, verbose_name="الكمية")
    session_key = models.CharField(max_length=255, verbose_name="مفتاح الجلسة")

    def __str__(self):
        return f"{self.product.name} × {self.quantity}"

    def get_total_price(self):
        """حساب المجموع الفرعي للعنصر"""
        return self.product.price * self.quantity
