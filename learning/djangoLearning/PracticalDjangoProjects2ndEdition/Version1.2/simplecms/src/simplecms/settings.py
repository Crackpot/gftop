#coding=utf8
# Django settings for simplecms project.
import os
from datetime import datetime

AKISMET_API_KEY = 'b8ce6230a51f'

# 获取项目路径
PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('高飞', 'gaofeitop@gmail.com'),
)

DELICIOUS_USER = ''
DELICIOUS_PASSWORD = ''

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'simplecms', # Or path to database file if using sqlite3.
        'USER': 'root', # Not used with sqlite3.
        'PASSWORD': '15263748', # Not used with sqlite3.
        'HOST': '', # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '', # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Asia/Shanghai'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'zh-CN'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(PROJECT_DIR, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

STATIC_CSS = os.path.join(MEDIA_ROOT, 'css')
STATIC_JS = os.path.join(MEDIA_ROOT, 'js')
STATIC_IMAGE = os.path.join(MEDIA_ROOT, 'images')
STATIC_THEMES = os.path.join(MEDIA_ROOT, 'themes')
STATIC_UPLOAD = os.path.join(MEDIA_ROOT, 'upload')
STATIC_EDITOR = os.path.join(MEDIA_ROOT, 'editor')

PHOTOLOGUE_DIR = os.path.join(MEDIA_ROOT, 'upload', 'photos', '%s' % datetime.now().strftime("%Y/%m/%d"))
ATTACHMENT_DIR = os.path.join(MEDIA_ROOT, 'upload', 'attachments', '%s' % datetime.now().strftime("%Y/%m/%d"))

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '=)@yk0ejmuf*-%dyjth$)9(b%dvfk@%je^(+mpw@iz^++)^n^)'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # 第三方中间件
    'debug_toolbar.middleware.DebugToolbarMiddleware', # debug_toolbar
)

# debug_toolbar ip设置
INTERNAL_IPS = ('127.0.0.1',)

# debug_toolbar面板设置
DEBUG_TOOLBAR_PANELS = (
    'debug_toolbar.panels.version.VersionDebugPanel',
    'debug_toolbar.panels.timer.TimerDebugPanel',
    'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
    'debug_toolbar.panels.headers.HeaderDebugPanel',
    'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
    'debug_toolbar.panels.template.TemplateDebugPanel',
    'debug_toolbar.panels.sql.SQLDebugPanel',
    'debug_toolbar.panels.signals.SignalDebugPanel',
    'debug_toolbar.panels.logger.LoggingPanel',
)

ROOT_URLCONF = 'simplecms.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_DIR, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.flatpages',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'debug_toolbar',
    'simplecms.cab',
    'simplecms.search',
    'simplecms.coltrane',
    'tagging',
    'django.contrib.comments', # 评论，创建表
    'django.contrib.markup',
    #'south', # migration
)
