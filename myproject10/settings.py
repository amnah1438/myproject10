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
    # 🧰 تطبيقات Django الأساسية
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 🌐 التطبيق الرئيسي للمتجر
    'core',         # 🏠 الصفحات العامة والإعدادات العامة للمتجر

    # 🧱 تطبيقات المتجر الإلكترونية
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
# 🌐 إعدادات الروابط والقوالب (Templates)
# ==============================
ROOT_URLCONF = 'myproject10.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        # 📁 مجلد القوالب العام
        'DIRS': [BASE_DIR / 'templates'],

        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
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
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
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
# 🖼️ الملفات الثابتة (Static Files)
# ==============================
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]  # ملفات التصميم العامة
STATIC_ROOT = BASE_DIR / "staticfiles"    # مكان تجميع الملفات عند النشر (collectstatic)


# ==============================
# 🧾 الملفات المرفوعة (Media Files)
# ==============================
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'           # مكان تخزين الملفات المرفوعة (صور/شعارات/منتجات)


# ==============================
# ⚙️ الإعداد الافتراضي لمفاتيح قاعدة البيانات
# ==============================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
