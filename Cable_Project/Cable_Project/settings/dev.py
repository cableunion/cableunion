# -*- coding: utf-8 -*-
"""
Django settings for Cable_Project project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'pi)0r)s&!!ptbl!+y)3dsc2$ix1n*1p&rw8(ge-n9o3jq-okm7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ckeditor',
    'ckeditor_uploader',
    'cable_trunk',
    'account',
    'common',
    'home',
    'category',
    'create_table',
    'article',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware', # admin
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.cache.CacheMiddleware',#for 全站缓存（针对视图及数据的不需要配置）
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.gzip.GZipMiddleware',# 处理gzip压缩,减轻服务器压力
)

ROOT_URLCONF = 'Cable_Project.urls'

WSGI_APPLICATION = 'Cable_Project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'trade',
        'USER': 'root',
        'PASSWORD': 'admin',
        'HOST': '', # null is localhost
        'PORT': '3306',
    }
}

AUTH_USER_MODEL = 'common.UserProfile'
# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'zh_CN'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

# from django.views.decorators.cache import cache_page 如果网页在缓存中显示缓存内容，否则生成访问的页面，保存在缓存中以便下次使用，显示缓存的页面。
AUTHENTICATION_BACKENDS = ('django.contrib.auth.backends.ModelBackend',)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR,  '../common/static'),
    os.path.join(BASE_DIR,  '../account/static'),
    os.path.join(BASE_DIR,  '../home/static'),
    os.path.join(BASE_DIR,  '../category/static'),
    os.path.join(BASE_DIR,  '../article/static'),
)

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), '../common/templates').replace('\\', '/'),
    os.path.join(os.path.dirname(__file__), '../account/templates').replace('\\', '/'),
    os.path.join(os.path.dirname(__file__), '../home/templates').replace('\\', '/'),
    os.path.join(os.path.dirname(__file__), '../category/templates').replace('\\', '/'),
    os.path.join(os.path.dirname(__file__), '../article/templates').replace('\\', '/'),
    # os.path.join(BASE_DIR,  '../common/templates'),
    # os.path.join(BASE_DIR,  '../account/templates'),
    # os.path.join(BASE_DIR,  '../home/templates'),
)

MEDIA_URL = '/static/images/category-introduce/'
MEDIA_ROOT = 'category/static/images/category-introduce/'
CKEDITOR_UPLOAD_PATH = STATIC_URL + '/article_images/' # ckeditor

SESSION_COOKIE_AGE = 60 * 60 # 60分钟
EMAIL_HOST = '' #SMTP地址
# EMAIL_PORT = 80 #SMTP端口
EMAIL_HOST_USER = '' #我自己的邮箱
EMAIL_HOST_PASSWORD = '' #我的邮箱密码
EMAIL_SUBJECT_PREFIX = u'[中缆联盟]' #为邮件Subject-line前缀,默认是'[django]'
EMAIL_USE_TLS = True #与SMTP服务器通信时，是否启动TLS链接(安全链接)。默认是false
#管理员站点
# SERVER_EMAIL = ''            #The email address that error messages come from, such as those sent to ADMINS and MANAGERS.