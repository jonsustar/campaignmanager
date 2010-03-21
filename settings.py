# Django settings for twibbots_django project.
import os


DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
     ('Jon', 'jon.sustar@gmail.com')
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'mysql'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = 'campaignmanager'             # Or path to database file if using sqlite3.
DATABASE_USER = 'twibbots_admin'             # Not used with sqlite3.
DATABASE_PASSWORD = 'passw0rd'         # Not used with sqlite3.
DATABASE_HOST = ''            # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

#LOGIN_REDIRECT_URL = '/admin/controlpanel'

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = ''

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'o%tbvl=r#0@l6&cn8wfiq2+t_s(_!vy)!t2#5b3=uaz&xv^m2k'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware'
)

ROOT_URLCONF = 'urls'

WEBSITE_ROOT = '/'

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

LOCAL_DATABASE_ROOT = '%s/bots/instances/databases' % PROJECT_ROOT

STATIC_DOC_ROOT = '%s/webroot' % PROJECT_ROOT

TEMPLATE_DIRS = ( '%s/webroot/templates' % PROJECT_ROOT )

CONVERSATIONS_PER_PAGE = 20

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.humanize',
    'django.contrib.sitemaps',
    'django.contrib.flatpages',
    'tinymce',
    'campaignmanager.websitemanager',
    #'pil'
    #'Image',
    #'filebrowser'
)

BASE_TITLE = "Twibbots: Twitter Bots with an attitude"

TINYMCE_JS_URL = '/js/tiny_mce/tiny_mce.js'

TINYMCE_JS_ROOT = '/js/tiny_mce'
TINYMCE_DEFAULT_CONFIG = {
    'theme': "advanced",
}

TINYMCE_FILEBROWSER = True

