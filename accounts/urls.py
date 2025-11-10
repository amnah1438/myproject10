# /Users/amnah/myproject10/accounts/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # ==============================
    # 🧩 روابط إدارة الحسابات
    # ==============================

    path('register/', views.register_view, name='register'),  # 🧾 إنشاء حساب جديد
    path('login/', views.login_view, name='login'),            # 🔐 تسجيل الدخول
]
