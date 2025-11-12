# ==============================
# 📦 /Users/amnah/myproject10/products/models.py
# ==============================

from django.db import models
from cloudinary.models import CloudinaryField  # ☁️ لرفع الصور إلى Cloudinary


# ==============================
# 🧩 نموذج التصنيفات
# ==============================
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="اسم التصنيف")
    description = models.TextField(blank=True, null=True, verbose_name="الوصف")

    class Meta:
        verbose_name = "تصنيف"
        verbose_name_plural = "التصنيفات"

    def __str__(self):
        return self.name


# ==============================
# 🛍️ نموذج المنتجات
# ==============================
class Product(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="التصنيف"
    )
    name = models.CharField(max_length=150, verbose_name="اسم المنتج")
    description = models.TextField(blank=True, null=True, verbose_name="الوصف")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="السعر")
    stock = models.PositiveIntegerField(verbose_name="الكمية المتاحة")

    # ☁️ رفع الصور إلى Cloudinary داخل مجلد 'products'
    # ✅ إضافة صورة افتراضية آمنة لتفادي الخطأ في makemigrations
    image = CloudinaryField(
        'صورة المنتج',
        folder='products',
        default='https://res.cloudinary.com/demo/image/upload/v1699999999/default.jpg',
        blank=True,
        null=True,
    )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإضافة")

    class Meta:
        verbose_name = "منتج"
        verbose_name_plural = "المنتجات"

    def __str__(self):
        return self.name
