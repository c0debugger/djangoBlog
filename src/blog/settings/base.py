

from pathlib import Path
import os

'''
####### ENVIRON SETUP and reading .env files ############################################################
'''
# import environ
# env = environ.Env(
#     # set casting, default value
#     DEBUG=(bool, False)
# )

# ENV_PATH = env.str('ENV_PATH','.env') # care about default here..

# # # reading .env file
# env.read_env(str(Path(__file__).resolve().parent)+ '/' + ENV_PATH)

# print(dir(env))
# '''
# ############################################################
# '''


import environ
env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
# reading .env file
environ.Env.read_env()
#print(dir(env))
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent
#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
 
# False if not in os.environ
DEBUG = env('DEBUG')


ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'django.contrib.sites', #added for All_AUTH

    #TinyMCE
    'tinymce',
    
    #fileBrowser
    'filebrowser',

    #timeZone
    'tz_detect',

    #Own
    'posts',
    'marketing',

    #All AUTH
    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    #djangoTweaks
    'widget_tweaks',

    #
    'crispy_forms',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', #whitenoise
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
    #TZ-DETECT package
    'tz_detect.middleware.TimezoneMiddleware',
]

ROOT_URLCONF = 'blog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
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

#ADDED For ALL_AUTH
AUTHENTICATION_BACKENDS = [
    
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
    
]



WSGI_APPLICATION = 'blog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': env.db(),
}




# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage' 

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL ='/media/'
STATICFILES_DIRS = [os.path.join(BASE_DIR,'static_in_env'),]

STATIC_ROOT = os.path.join(os.path.dirname(
    BASE_DIR), "static_cdn", "static_root")


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(os.path.dirname(
    BASE_DIR), "static_cdn", "media_root")




# VENV_PATH = os.path.dirname(BASE_DIR)
# STATIC_ROOT = os.path.join(BASE_DIR,'static_root')
# MEDIA_ROOT = os.path.join(BASE_DIR,'media_root')
#print(f'BASE ={BASE_DIR}')
# print(f'STATICFILES_DIR ={STATICFILES_DIRS} /n')
# print(f'VENV_PATH ={VENV_PATH} /n')
# print(f'STATIC_ROOT ={STATIC_ROOT} /n')
# print(f'MEDIA_ROOT ={STATIC_ROOT} /n')


### TinyMCE

TINYMCE_DEFAULT_CONFIG = {
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 20,
    'selector': 'textarea',
    'theme': 'modern',
    'plugins': '''
            textcolor save link image media preview codesample contextmenu
            table code lists fullscreen  insertdatetime  nonbreaking
            contextmenu directionality searchreplace wordcount visualblocks
            visualchars code fullscreen autolink lists  charmap print  hr
            anchor pagebreak
            ''',
    'toolbar1': '''
            fullscreen preview bold italic underline | fontselect,
            fontsizeselect  | forecolor backcolor | alignleft alignright |
            aligncenter alignjustify | indent outdent | bullist numlist table |
            | link image media | codesample |
            ''',
    'toolbar2': '''
            visualblocks visualchars |
            charmap hr pagebreak nonbreaking anchor |  code |
            ''',
    'contextmenu': 'formats | link image',
    'menubar': True,
    'statusbar': True,
    'width': 'auto',
}


SITE_ID = 1

# Provider specific settings
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        # For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:
        'APP': {
            'client_id': '123',
            'secret': '456',
            'key': ''
        }
    }
}

CRISPY_TEMPLATE_PACK = 'bootstrap4'


#django allauth settings
ACCOUNT_EMAIL_REQUIRED=True
ACCOUNT_AUTHENTICATION_METHOD= 'username_email'
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_LOGOUT_REDIRECT_URL ='/accounts/login/'
LOGIN_REDIRECT_URL = '/'


#print(os.environ.values)



#EMAIL_URL =env('EMAIL_URL')
EMAIL_BACKEND = env('EMAIL_BACKEND')

EMAIL_CONFIG = env.email_url('EMAIL_URL')
#print(EMAIL_CONFIG)
# print("-------------------------------------------------------\n")
# print(vars())
vars().update(EMAIL_CONFIG)
# print(EMAIL_CONFIG)
#EMAIL_HOST = EMAIL_CONFIG['EMAIL_HOST']
# print("-------------------------------------------------------\n")
# print(vars())

#print(EMAIL_CONFIG['EMAIL_HOST_USER'])

EMAIL_HOST =EMAIL_CONFIG['EMAIL_HOST']
EMAIL_PORT =EMAIL_CONFIG['EMAIL_PORT']
#EMAIL_USE_TLS = env('EMAIL_USE_TLS')
EMAIL_HOST_USER = EMAIL_CONFIG['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD =EMAIL_CONFIG['EMAIL_HOST_PASSWORD']
SENDER = env('SENDER')
RECEIVERS = env('RECEIVERS')
