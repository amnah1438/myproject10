from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


# ==============================
# 🌐 روابط المشروع الأساسية
# ==============================
urlpatterns = [
    # ==============================
    # 🧭 لوحة التحكم الإدارية
    # ==============================
    path('admin/', admin.site.urls),

    # ==============================
    # 🌐 التطبيق الرئيسي (واجهة المتجر)
    # ==============================
    path('', include('core.urls')),  # 🏠 الصفحة الرئيسية والصفحات العامة

    # ==============================
    # 🧩 تطبيقات المتجر الداخلية
    # ==============================
   path('accounts/', include('accounts.urls')),  # 👥 إدارة المستخدمين والعملاء
    path('products/', include('products.urls')),  # 🛍️ إدارة المنتجات والمتجر
    path('orders/', include('orders.urls')),      # 📦 إدارة الطلبات والدفع
    path('cart/', include('cart.urls')),          # 🛒 إدارة السلة
]


# ==============================
# 🖼️ إعداد عرض الملفات الثابتة والمرفوعة أثناء التطوير
# ==============================
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
