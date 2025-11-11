from pathlib import Path
import os
import cloudinary
import cloudinary.uploader
import cloudinary.api
from django.core.management.utils import get_random_secret_key

# ==============================
# 📁 المسار الأساسي للمشروع
# ==============================
BASE_DIR = Path(__file__).resolve().parent.parent

# ==============================
# 🔐 المفتاح السري
# ==============================
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', get_random_secret_key())

# ==============================
# ⚙️ وضع التصحيح والاستضافة
# ==============================
DEBUG = os.getenv('DJANGO_DEBUG', 'True') == 'True'
ALLOWED_HOSTS = ["127.0.0.1", "localhost", ".onrender.com"]

# ==============================
# 🧩 التطبيقات
# ==============================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 🌐 تطبيقات المشروع
    'core',
    'accounts',
    'products',
    'orders',

    # ☁️ تطبيقات Cloudinary
    'cloudinary',
    'cloudinary_storage',
]

# ==============================
# 🧱 الوسطاء
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
# 🌐 القوالب
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
# ⚙️ إعداد قاعدة التطوير (SQLite)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ⚙️ إعداد قاعدة الإنتاج (PostgreSQL)
if os.getenv("DJANGO_ENV") == "production":
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'HOST': 'dpg-d49lo93e5dus73cqfp20-a',
            'PORT': '5432',
            'NAME': 'db_myproject10',
            'USER': 'db_myproject10_user',
            'PASSWORD': '7BTGjAyNu7diRi9WilNYV48eFeGwoL2M',
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
# 🖼️ الملفات الثابتة والميديا
# ==============================
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"

cloudinary.config(
    cloud_name="dyg4401o9",
    api_key="283452178212273",
    api_secret="hRYpVPeOwKcCDSruJ9Um_56WdVw",
    secure=True
)

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
MEDIA_URL = '/media/'

# ==============================
# ⚙️ الإعداد الافتراضي للمفاتيح
# ==============================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
