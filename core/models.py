from django.db import models

class SiteSettings(models.Model):
    site_name = models.CharField(max_length=200, verbose_name="اسم الموقع")
    logo = models.ImageField(upload_to='logos/', blank=True, null=True, verbose_name="الشعار")
    contact_email = models.EmailField(verbose_name="البريد الإلكتروني للتواصل")
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="رقم الهاتف")
    address = models.TextField(blank=True, null=True, verbose_name="العنوان")
    about = models.TextField(blank=True, null=True, verbose_name="عن المتجر")

    class Meta:
        verbose_name = "إعداد المتجر"
        verbose_name_plural = "إعدادات المتجر"

    def __str__(self):
        return self.site_name
