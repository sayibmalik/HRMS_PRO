import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-htklxm@g)c2(+z^%vk0-un0&_#dwb@vx-9-#fohm^+y#57_x&u'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['hr.defconinnovations.com','hrms.defconinnovations.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_countries',
    'home',
    'schedule',
    'Attendance',
    'Employee',
    'HR',
    'Leaves',
    'Payroll',
    'Project',
    'Setting',
    'timesheets',
    'Site',
    'SelfServices',
    'Decisions',
    'MuqeemServices',
    'Recruitment',
    'Training',
    'Memos',
    'Policies',
    'Support',
    'conf',
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

ROOT_URLCONF = 'ZHR.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'ZHR.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases



if DEBUG:
    print("Development")
    # DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'sampledb.sqlite3'),
    #     }
    # }
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'hrms_dev',
            'USER': 'hrms_devuser',
            'PASSWORD': 'Zainab321#',
            'HOST': '89.116.20.12',
            'PORT': '5432',
        }
    }
    # DATABASES = {
    #     'default': {
    #         'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #         'NAME': 'proerp',
    #         'USER': 'proerpuser',
    #         'PASSWORD': 'Kashmir@2021',
    #         'HOST': '159.89.206.182',
    #         'PORT': '5432',
    #     }
    # }
    
else:
    print("Production")
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.environ['proerp_database'],
            'USER': os.environ['proerp_username'],
            'PASSWORD': os.environ['proerp_password'],
            'HOST': os.environ['proerp_host'],
            'PORT': os.environ['proerp_port'],
        }
    }



# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'rdaqib@gmail.com'
EMAIL_HOST_PASSWORD = 'Evilpunk@20'


STRIPE_PUBLIC_KEY="pk_test_51Iol7RSBPtfBRXFP1uW9pHW6VSv9m1AJ6HmzonN5lkEFfYg1us1VYErvHWliXDHogbWwqmHY1BvDN8PN2gTIapw000Iwv8reRx"
STRIPE_SECRET_KEY="sk_test_51Iol7RSBPtfBRXFPkrBadw6KemqTO5x5lrxzBOspFidPvPjxXs1CCzfNqsF6VcRRijF57KkHA5NNnFbXjVVoiU5f0011RqLiyf"
STRIPE_WEBHOOK_SECRET = ""