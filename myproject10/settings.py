from pathlib import Path

# ==============================
# 📁 المسار الأساسي للمشروع
# ==============================
BASE_DIR = Path(__file__).resolve().parent.parent


# ==============================
# 🔐 إعداد المفتاح السري
# ==============================
SECRET_KEY = 'django-insecure-6$2z-1!q4vyti7lq++$m^r-p$_y5k%=b11-z+76s29&1(mp9ve'


# ==============================
# ⚙️ إعدادات التصحيح والاستضافة
# ==============================
DEBUG = True
ALLOWED_HOSTS = []


# ==============================
# 🧩 التطبيقات المثبتة
# ==============================
INSTALLED_APPS = [
    # تطبيقات Django الافتراضية
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # ==============================
    # 🌐 التطبيق الرئيسي للمتجر
    # ==============================
    'core',         # 🏠 الصفحة الرئيسية والصفحات العامة

    # ==============================
    # 🧱 تطبيقات المتجر الإلكترونية
    # ==============================
    'accounts',     # 👥 إدارة المستخدمين والعملاء
    'products',     # 🛍️ إدارة المنتجات والمخزون
    'orders',       # 🧾 إدارة الطلبات والسلة والدفع
]


# ==============================
# 🧱 إعدادات الوسطاء (Middleware)
# ==============================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# ==============================
# 🌐 إعدادات الروابط والقوالب
# ==============================
ROOT_URLCONF = 'myproject10.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # مجلد القوالب العامة
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'myproject10.wsgi.application'


# ==============================
# 🗃️ إعدادات قاعدة البيانات
# ==============================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# ==============================
# 🔒 إعدادات كلمات المرور
# ==============================
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# ==============================
# 🌍 اللغة والمنطقة الزمنية
# ==============================
LANGUAGE_CODE = 'ar'            # اللغة الافتراضية: العربية
TIME_ZONE = 'Asia/Riyadh'       # التوقيت المحلي: الرياض
USE_I18N = True                 # تفعيل الترجمة الدولية
USE_L10N = True                 # تفعيل تنسيق اللغة المحلية
USE_TZ = True                   # تفعيل المنطقة الزمنية


# ==============================
# 🖼️ الملفات الثابتة
# ==============================
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / "static"]


# ==============================
# 🧾 الإعداد الافتراضي لمفاتيح قاعدة البيانات
# ==============================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
