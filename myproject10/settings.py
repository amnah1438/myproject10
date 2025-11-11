from pathlib import Path
import cloudinary
import cloudinary.uploader
import cloudinary.api

# ==============================
# 📁 المسار الأساسي للمشروع
# ==============================
BASE_DIR = Path(__file__).resolve().parent.parent

# ==============================
# 🔐 المفتاح السري للمشروع
# ==============================
SECRET_KEY = 'django-insecure-6$2z-1!q4vyti7lq++$m^r-p$_y5k%=b11-z+76s29&1(mp9ve'

# ==============================
# ⚙️ إعدادات التصحيح والاستضافة
# ==============================
DEBUG = True
ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

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

    # 🌐 تطبيقات المتجر
    'core',
    'accounts',
    'products',
    'orders',

    # ☁️ تطبيقات Cloudinary
    'cloudinary',
    'cloudinary_storage',
]

# ==============================
# 🧱 الوسائط (Middleware)
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
# 🌐 إعداد القوالب
# ==============================
ROOT_URLCONF = 'myproject10.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
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
# 🗃️ قاعدة البيانات
# ==============================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ==============================
# 🔒 إعداد كلمات المرور
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
LANGUAGE_CODE = 'ar'
TIME_ZONE = 'Asia/Riyadh'
USE_I18N = True
USE_TZ = True

# ==============================
# 🖼️ الملفات الثابتة (Static)
# ==============================
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"

# ==============================
# ☁️ إعداد Cloudinary كمخزن للميديا
# ==============================
cloudinary.config(
    cloud_name="dyg4401o9",          # 👈 اسم حسابك في Cloudinary
    api_key="283452178212273",       # 👈 المفتاح الخاص بك
    api_secret="hRYpVPeOwKcCDSruJ9Um_56WdVw",  # 👈 الرمز السري
    secure=True
)

# ✅ جعل Cloudinary هو المخزن الافتراضي للملفات المرفوعة
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# 🧾 مسار الميديا (للدعم فقط، لا يتم التخزين محليًا)
MEDIA_URL = '/media/'

# ❌ لا يوجد MEDIA_ROOT لأن Cloudinary يتولى التخزين السحابي
# (إزالة هذا السطر مهم جدًا حتى لا يحفظ Django محليًا)

# ==============================
# ⚙️ الإعداد الافتراضي للمفاتيح
# ==============================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
