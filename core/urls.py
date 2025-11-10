from django.urls import path
from . import views

urlpatterns = [
    # 🏠 الصفحة الرئيسية للموقع
    path('', views.home, name='home'),
]
