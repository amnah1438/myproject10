from django.urls import path


urlpatterns = [
    path('', views.cart_view, name='cart'),
]
