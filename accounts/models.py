from django.db import models
from django.contrib.auth.models import User

class CustomerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="المستخدم")
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="رقم الجوال")
    address = models.CharField(max_length=255, blank=True, null=True, verbose_name="العنوان")
    city = models.CharField(max_length=100, blank=True, null=True, verbose_name="المدينة")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإنشاء")

    class Meta:
        verbose_name = "ملف عميل"
        verbose_name_plural = "ملفات العملاء"

    def __str__(self):
        return self.user.username
