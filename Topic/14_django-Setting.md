# Django Settings.py - সম্পূর্ণ গাইড


## Django Settings Documentation


- [1. Settings.py কি?](#1-settingspy-কি)
- [2. বেসিক সেটিংস](#2-বেসিক-সেটিংস)
- [3. Database Configuration](#3-database-configuration)
- [4. Installed Apps](#4-installed-apps)
- [5. Middleware](#5-middleware)
- [6. Templates Configuration](#6-templates-configuration)
- [7. Static Files (CSS, JavaScript, Images)](#7-static-files-css-javascript-images)
- [8. Media Files (User Uploads)](#8-media-files-user-uploads)
- [9. Authentication & User Model](#9-authentication--user-model)
- [10. Internationalization (i18n)](#10-internationalization-i18n)
- [11. Email Configuration](#11-email-configuration)
- [12. Security Settings (Production)](#12-security-settings-production)
- [13. Caching (Dummy-redic-memcached)](#13-caching-dummy-redic-memcached)
- [14. Session Configuration](#14-session-configuration)
- [15. Logging](#15-logging)
- [16. REST Framework Settings](#16-rest-framework-settings)
- [17. CORS Settings](#17-cors-settings)
- [18. File Upload Settings](#18-file-upload-settings)
- [19. Celery Configuration (Async Tasks)](#19-celery-configuration-async-tasks)
- [20. Custom Settings](#20-custom-settings)
- [21. Environment-based Configuration](#21-environment-based-configuration)
- [22. Environment Variables (env-file)](#22-environment-variables-env-file)
- [23. Testing Settings](#23-testing-settings)
- [24. AWS S3 Configuration (Media Files)](#24-aws-s3-configuration-media-files)
- [Useful Commands](#useful-commands)

---

<br>
<br>
<br> 





## 1. Settings.py কি?
[Home](#django-settings-documentation)

`settings.py` হলো Django প্রজেক্টের কনফিগারেশন ফাইল। এখানে আপনার অ্যাপ্লিকেশনের সব সেটিংস থাকে।

---

<br>
<br>
<br> 

## 2. বেসিক সেটিংস
[Home](#django-settings-documentation)

### DEBUG Mode
```python
# Development এ True রাখুন, Production এ False
DEBUG = True

# DEBUG False হলে এটা দিতে হবে
ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'yourdomain.com']
```

**ব্যাখ্যা:**
- `DEBUG = True` মানে ডেভেলপমেন্ট মোড। এরর দেখাবে বিস্তারিত।
- Production এ অবশ্যই `False` করতে হবে নিরাপত্তার জন্য।

### SECRET_KEY
```python
# এটা গোপন রাখতে হবে। Production এ environment variable ব্যবহার করুন
SECRET_KEY = 'django-insecure-your-secret-key-here'

# Better approach (Production):
import os
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')
```

**গুরুত্ব:** এটা Django এর cryptographic signing এ ব্যবহার হয়। লিক হলে নিরাপত্তা ঝুঁকি।

---

<br>
<br>
<br> 


## 3. Database Configuration
[Home](#django-settings-documentation)

### SQLite (Default)
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

### PostgreSQL
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydatabase',
        'USER': 'mydatabaseuser',
        'PASSWORD': 'mypassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### MySQL
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mydatabase',
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'charset': 'utf8mb4',
        }
    }
}
```

### Multiple Databases
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'main_db',
    },
    'users_db': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'users_database',
    }
}
```

---
<br>
<br>
<br>
<br>
<br>



## 4. Installed Apps
[Home](#django-settings-documentation)

```python
INSTALLED_APPS = [
    # Django এর built-in apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Third-party apps
    'rest_framework',
    'corsheaders',
    'django_filters',
    
    # আপনার নিজের apps
    'myapp',
    'users',
    'products',
]
``` 

---
<br>
<br>
<br>
<br>
<br>


## 5. Middleware
[Home](#django-settings-documentation)

```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',  # CORS এর জন্য
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
    # Custom middleware
    # 'myapp.middleware.CustomMiddleware',
]
```

**ব্যাখ্যা:** Middleware হলো request-response এর মাঝে চলা কোড। Order গুরুত্বপূর্ণ!

---

<br>
<br>
<br>
<br>
<br>


## 6. Templates Configuration
[Home](#django-settings-documentation)

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # আপনার template folder
        'APP_DIRS': True,  # প্রতিটি app এর templates folder চেক করবে
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                
                # Custom context processor
                # 'myapp.context_processors.custom_processor',
            ],
        },
    },
]
```

---

<br>
<br>
<br>
<br>
<br>


## 7. Static Files (CSS, JavaScript, Images)
[Home](#django-settings-documentation)

```python
# URL যেখানে static files পাওয়া যাবে
STATIC_URL = '/static/'

# Development এ static files খোঁজার path
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# Production এ collectstatic চালালে এখানে জমা হবে
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Static files finder
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]
```

---
<br>
<br>
<br>
<br>
<br>



## 8. Media Files (User Uploads)
[Home](#django-settings-documentation)

```python
# User uploaded files এর URL
MEDIA_URL = '/media/'

# User uploaded files save হবে এখানে
MEDIA_ROOT = BASE_DIR / 'media'
```

**urls.py তে যুক্ত করতে হবে:**
```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # আপনার URLs
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

---

<br>
<br>
<br>
<br>
<br>



## 9. Authentication & User Model
[Home](#django-settings-documentation)

### Default Auth Settings
```python
# Login করার পর কোথায় redirect হবে
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/login/'

# Login page এর URL
LOGIN_URL = '/login/'

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 8,
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
```

### Custom User Model
```python
# Custom user model ব্যবহার করলে
AUTH_USER_MODEL = 'myapp.CustomUser'
```

---

## 10. Internationalization (i18n)
[Home](#django-settings-documentation)

<br>
<br>
<br>
<br>
<br>



```python
# Language code
LANGUAGE_CODE = 'bn'  # বাংলার জন্য 'bn', ইংরেজির জন্য 'en-us'

# Timezone
TIME_ZONE = 'Asia/Dhaka'  # বাংলাদেশ timezone

# Enable internationalization
USE_I18N = True

# Enable timezone support
USE_TZ = True

# Available languages
LANGUAGES = [
    ('en', 'English'),
    ('bn', 'বাংলা'),
]

# Locale paths
LOCALE_PATHS = [
    BASE_DIR / 'locale',
]
```

---
<br>
<br>
<br>
<br>
<br>


## 11. Email Configuration
[Home](#django-settings-documentation)

### Console Backend (Development)
```python
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```

### SMTP (Production)
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-password'
DEFAULT_FROM_EMAIL = 'noreply@yourdomain.com'
```

### SendGrid
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = 'your-sendgrid-api-key'
```

---
<br>
<br>
<br>
<br>
<br>


## 12. Security Settings (Production)
[Home](#django-settings-documentation)

```python
# HTTPS সেটিংস
SECURE_SSL_REDIRECT = True  # HTTP থেকে HTTPS এ redirect
SESSION_COOKIE_SECURE = True  # Cookie শুধু HTTPS এ পাঠাবে
CSRF_COOKIE_SECURE = True

# HSTS (HTTP Strict Transport Security)
SECURE_HSTS_SECONDS = 31536000  # 1 বছর
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Security headers
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'

# CSRF
CSRF_COOKIE_HTTPONLY = True
CSRF_TRUSTED_ORIGINS = ['https://yourdomain.com']
```

---
<br>
<br>
<br>
<br>
<br>


## 13. Caching (Dummy Redic Memcached)
[Home](#django-settings-documentation)

### Dummy Cache (Development)
```python
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}
```

### Redis Cache (Production)
```python
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        },
        'KEY_PREFIX': 'myapp',
        'TIMEOUT': 300,  # 5 minutes
    }
}
```

### Memcached
```python
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.PyMemcacheCache',
        'LOCATION': '127.0.0.1:11211',
    }
}
```

---
<br>
<br>
<br>
<br>
<br>



## 14. Session Configuration
[Home](#django-settings-documentation)

```python
# Session engine
SESSION_ENGINE = 'django.contrib.sessions.backends.db'  # Database
# SESSION_ENGINE = 'django.contrib.sessions.backends.cache'  # Cache
# SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'  # Cache + DB

# Session cookie age (seconds)
SESSION_COOKIE_AGE = 1209600  # 2 weeks

# Browser বন্ধ করলে session শেষ হবে কিনা
SESSION_EXPIRE_AT_BROWSER_CLOSE = False

# Session cookie name
SESSION_COOKIE_NAME = 'sessionid'
```

---
<br>
<br>
<br>
<br>
<br>



## 15. Logging
[Home](#django-settings-documentation)

```python
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
        'file': {
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'logs/django.log',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
        },
        'myapp': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
        },
    },
}
```

---
<br>
<br>
<br>
<br>
<br>



## 16. REST Framework Settings
[Home](#django-settings-documentation)

```python
REST_FRAMEWORK = {
    # Authentication
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    
    # Permissions
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    
    # Pagination
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    
    # Filtering
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ],
    
    # Throttling (Rate limiting)
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle',
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '100/day',
        'user': '1000/day',
    },
}
```

---
<br>
<br>
<br>
<br>
<br>



## 17. CORS Settings
[Home](#django-settings-documentation)

```python
# CORS headers (Frontend থেকে API call এর জন্য)
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://localhost:8080",
    "https://yourdomain.com",
]

# অথবা সব origin allow করতে (নিরাপদ নয়!)
# CORS_ALLOW_ALL_ORIGINS = True

# Credentials allow করতে
CORS_ALLOW_CREDENTIALS = True

# যে HTTP methods allow করবেন
CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]

# Headers
CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]
```

---
<br>
<br>
<br>
<br>
<br>



## 18. File Upload Settings
[Home](#django-settings-documentation)

```python
# Maximum file upload size (bytes)
FILE_UPLOAD_MAX_MEMORY_SIZE = 5242880  # 5 MB

# যেখানে temporary files রাখবে
FILE_UPLOAD_TEMP_DIR = '/tmp/'

# File upload permissions
FILE_UPLOAD_PERMISSIONS = 0o644
FILE_UPLOAD_DIRECTORY_PERMISSIONS = 0o755

# Allowed file extensions (custom validation দরকার)
ALLOWED_IMAGE_TYPES = ['jpg', 'jpeg', 'png', 'gif']
ALLOWED_DOCUMENT_TYPES = ['pdf', 'doc', 'docx', 'txt']
```

---
<br>
<br>
<br>
<br>
<br>



## 19. Celery Configuration (Async Tasks)
[Home](#django-settings-documentation)

```python
# Celery broker URL
CELERY_BROKER_URL = 'redis://localhost:6379/0'

# Result backend
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'

# Task serialization
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT = ['json']

# Timezone
CELERY_TIMEZONE = 'Asia/Dhaka'

# Task time limit
CELERY_TASK_TIME_LIMIT = 30 * 60  # 30 minutes
```

---
<br>
<br>
<br>
<br>
<br>



## 20. Custom Settings
[Home](#django-settings-documentation)

```python
# আপনার নিজের custom settings

SITE_NAME = 'My Awesome Site'
ADMIN_EMAIL = 'admin@example.com'
ITEMS_PER_PAGE = 20

# Payment gateway settings
PAYMENT_GATEWAY_API_KEY = os.environ.get('PAYMENT_API_KEY')
PAYMENT_GATEWAY_SECRET = os.environ.get('PAYMENT_SECRET')

# SMS gateway
SMS_API_KEY = os.environ.get('SMS_API_KEY')
```

---
<br>
<br>
<br>
<br>
<br>



## 21. Environment-based Configuration
[Home](#django-settings-documentation)

### Development vs Production Settings

**settings/base.py:**
```python
# Common settings
SECRET_KEY = os.environ.get('SECRET_KEY')
INSTALLED_APPS = [...]
MIDDLEWARE = [...]
```

**settings/development.py:**
```python
from .base import *

DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

**settings/production.py:**
```python
from .base import *

DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT'),
    }
}

# Security settings
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
```

**ব্যবহার:**
```bash
# Development
python manage.py runserver --settings=myproject.settings.development

# Production
python manage.py runserver --settings=myproject.settings.production
```

---
<br>
<br>
<br>
<br>
<br>



## 22. Environment Variables (.env file)
[Home](#django-settings-documentation)

**.env ফাইল:**
```
SECRET_KEY=your-secret-key-here
DEBUG=True
DATABASE_URL=postgresql://user:password@localhost:5432/dbname
ALLOWED_HOSTS=localhost,127.0.0.1

# Email
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-password

# AWS S3
AWS_ACCESS_KEY_ID=your-access-key
AWS_SECRET_ACCESS_KEY=your-secret-key
AWS_STORAGE_BUCKET_NAME=your-bucket
```

**settings.py তে ব্যবহার (python-decouple):**
```python
from decouple import config, Csv

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())
```

---
<br>
<br>
<br>
<br>
<br>



## 23. Testing Settings
[Home](#django-settings-documentation)

```python
# Test runner
TEST_RUNNER = 'django.test.runner.DiscoverRunner'

# Test database
if 'test' in sys.argv:
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }

# Password hashers (testing এ fast করার জন্য)
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.MD5PasswordHasher',
]
```

---
<br>
<br>
<br>
<br>
<br>



## 24. AWS S3 Configuration (Media Files)
[Home](#django-settings-documentation)

```python
# django-storages দরকার: pip install django-storages boto3

# Storage backends
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# AWS settings
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = 'your-bucket-name'
AWS_S3_REGION_NAME = 'ap-south-1'  # Mumbai region

# Optional settings
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
AWS_DEFAULT_ACL = 'public-read'
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
```

---
<br>
<br>
<br>
<br>
<br>



## 25. Important Tips & Best Practices
[Home](#django-settings-documentation)

### ✅ করণীয়:
1. **SECRET_KEY গোপন রাখুন** - Environment variable ব্যবহার করুন
2. **Production এ DEBUG = False** রাখুন
3. **ALLOWED_HOSTS** সঠিকভাবে configure করুন
4. **Security settings** enable করুন production এ
5. **Environment-based** settings ব্যবহার করুন
6. **.env file** use করুন sensitive data এর জন্য
7. **Logging** setup করুন error tracking এর জন্য

### ❌ করবেন না:
1. SECRET_KEY কখনো GitHub এ push করবেন না
2. Production এ DEBUG = True রাখবেন না
3. Default database password ব্যবহার করবেন না
4. Sensitive data hardcode করবেন না
5. CORS_ALLOW_ALL_ORIGINS = True production এ ব্যবহার করবেন না


---

<br>
<br>
<br>
<br>
<br>



### Useful Commands
[Home](#django-settings-documentation)

```bash
# Settings check করুন
python manage.py check --deploy

# Security check
python manage.py check --deploy --settings=production

# Static files collect করুন
python manage.py collectstatic

# Database migrate
python manage.py migrate

# Create superuser
python manage.py createsuperuser
```

---
<br>

**Django Documentation**  - https://docs.djangoproject.com/