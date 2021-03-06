import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CART_SESSION_ID = 'cart'  # 用于我们的会话中来储存购物车。因为 Django 的会话对于每个访问者是独立的,我们可以在所有的会话中使用相同的会话键。

############# 发送邮件 ###############3
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = False
EMAIL_PORT = 25
EMAIL_HOST = 'smtp.163.com'
EMAIL_HOST_USER = 'hanqianops@163.com'
EMAIL_HOST_PASSWORD = ''
DEFAULT_FROM_EMAIL = 'hanqianops@163.com'

########## Celery ##################
BROKER_URL = 'amqp://guest:guest@10.240.1.103//'
CELERY_RESULT_BACKEND = 'amqp://guest:guest@10.240.1.103//'
TASK_SERIALIZER = 'json'
ACCEPT_CONTENT = ['json']

SECRET_KEY = 'c63=g$cy7xkylf_*a5x3bjhq5ya0^-%9q3&pa7+!9syn)qpd^c'
DEBUG = True
ALLOWED_HOSTS = ["*"]

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'shop',
    'cart',
    'orders',
    'coupons',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myshop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'cart.context_processors.cart',   # 模板上下文处理器，可以在任何地方使用该上下文
            ],
        },
    },
]

WSGI_APPLICATION = 'myshop.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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


LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True



MEDIA_URL = '/static/media/'   # 图片访问路径
MEDIA_ROOT = os.path.join(BASE_DIR, 'static/media')  # 图片保存路径，MEDIA_ROOT+upload_to

STATIC_URL = '/static/'
STATICFILES_DIRS=(
    os.path.join(BASE_DIR,"static"),
)