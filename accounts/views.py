from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django import forms


# ==============================
# 🧾 نموذج إنشاء حساب جديد (Register Form)
# ==============================
class RegisterForm(forms.ModelForm):
    password = forms.CharField(
        label="كلمة المرور",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'أدخل كلمة المرور'
        })
    )
    password_confirm = forms.CharField(
        label="تأكيد كلمة المرور",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'أدخل تأكيد كلمة المرور'
        })
    )

    class Meta:
        model = User
        fields = ['username', 'email']
        labels = {
            'username': 'اسم المستخدم',
            'email': 'البريد الإلكتروني',
        }
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'اسم المستخدم'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'البريد الإلكتروني'
            }),
        }

    def clean(self):
        """التحقق من تطابق كلمتي المرور"""
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        if password != password_confirm:
            raise forms.ValidationError("⚠️ كلمتا المرور غير متطابقتين.")
        return cleaned_data


# ==============================
# 🧩 إنشاء حساب جديد (Register View)
# ==============================
def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, "✅ تم إنشاء الحساب بنجاح! يمكنك الآن تسجيل الدخول.")
            return redirect('login')
        else:
            messages.error(request, "⚠️ حدث خطأ في البيانات، يرجى التحقق.")
    else:
        form = RegisterForm()

    return render(request, 'accounts-templates/register.html', {'form': form})


# ==============================
# 🔐 تسجيل الدخول (Login View)
# ==============================
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, f"👋 مرحبًا {username}! تم تسجيل الدخول بنجاح.")
                return redirect('/')
            else:
                messages.error(request, "❌ اسم المستخدم أو كلمة المرور غير صحيحة.")
        else:
            messages.error(request, "⚠️ تحقق من البيانات المدخلة.")
    else:
        form = AuthenticationForm()

    return render(request, 'accounts-templates/login.html', {'form': form})


# ==============================
# 🚪 تسجيل الخروج (Logout View)
# ==============================
def logout_view(request):
    logout(request)
    messages.info(request, "👋 تم تسجيل الخروج بنجاح.")
    return redirect('login')
