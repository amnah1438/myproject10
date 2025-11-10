from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>مرحبًا بكِ في الصفحة الرئيسية للمتجر الإلكتروني 🛍️</h1>")
