from pathlib import Path
import os
from dotenv import load_dotenv
import cloudinary
import cloudinary.uploader
import cloudinary.api
from django.core.management.utils import get_random_secret_key

# ==============================
# 📦 تحميل ملف .env
# ==============================
load_dotenv()

# ==============================
# 📁 المسار الأساسي للمشروع
# ==============================
BASE_DIR = Path(__file__).resolve().parent.parent

# ==============================
# 🔐 المفتاح السري
# ==============================
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", get_random_secret_key())

# ==============================
# ⚙️ وضع التصحيح والاستضافة
# ==============================
DEBUG = os.getenv("DJANGO_DEBUG", "True") == "True"

# 👇 السماح تلقائي بكل نطاق فرعي من Render + النطاقات المحلية
ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
    os.getenv("RENDER_EXTERNAL_HOSTNAME", ""),  # يسمح تلقائيًا بنطاق Render الحالي
    ".onrender.com",  # لأي نطاق فرعي آخر داخل Render
]

# ==============================
# 🧩 التطبيقات المثبتة
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
    'cart',

    # ☁️ تطبيقات Cloudinary
    'cloudinary',
    'cloudinary_storage',
]

# ==============================
# 🧱 الوسطاء (Middleware)
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
# 🗃️ قواعد البيانات
# ==============================
if os.getenv("DJANGO_ENV") == "production":
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'HOST': os.getenv('DB_HOST'),
            'PORT': os.getenv('DB_PORT'),
            'NAME': os.getenv('DB_NAME'),
            'USER': os.getenv('DB_USER'),
            'PASSWORD': os.getenv('DB_PASSWORD'),
        }
    }
else:
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
# 🖼️ الملفات الثابتة والميديا
# ==============================
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"

# ☁️ Cloudinary
cloudinary.config(
    cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
    api_key=os.getenv("CLOUDINARY_API_KEY"),
    api_secret=os.getenv("CLOUDINARY_API_SECRET"),
    secure=True
)

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
MEDIA_URL = '/media/'

# ==============================
# ⚙️ الإعداد الافتراضي للمفاتيح
# ==============================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
