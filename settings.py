import os

abspath = lambda *p: os.path.abspath(os.path.join(*p))
PROJECT_ROOT = abspath(os.path.dirname(__file__))
DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Marlon Mantilla', 'marman0315@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'cittybox_db',                      # Or path to database file if using sqlite3.
        'USER': 'marman',                      # Not used with sqlite3.
        'PASSWORD': 'asdasd',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}


TIME_ZONE = 'America/Bogota'
LANGUAGE_CODE = 'es-CO'

ugettext = lambda s: s
LANGUAGES = (
    ('en', ugettext('English')),
    ('nl', ugettext('Dutch')),
    ('fr', ugettext('French')),
    ('pl', ugettext('Polish')),
    ('pt', ugettext('Portugese')),
    ('es', ugettext('Spanish')),
)

SITE_ID = 1


USE_I18N = True
USE_L10N = True


MEDIA_ROOT = abspath(PROJECT_ROOT, 'media')
MEDIA_URL = '/media/'


# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = '/media/admin/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'e)zcsixtu5xl(04w=qtkm0+eb%$4&wx(%ti#=b-dxjqv3p*)ug'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'userena.middleware.UserenaLocaleMiddleware',
)
TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",
)

AUTHENTICATION_BACKENDS = (
    'userena.backends.UserenaAuthenticationBackend',
    'guardian.backends.ObjectPermissionBackend',
    'django.contrib.auth.backends.ModelBackend',
)

ROOT_URLCONF = 'cb_project.urls'

TEMPLATE_DIRS = (
    abspath(PROJECT_ROOT, 'templates')
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'easy_thumbnails',
    'guardian',
    'south',
    'userena',
    'userena.contrib.umessages',
    'profiles',
    'offers',
	'shippings',
    'debug_toolbar',
	'widget_tweaks',
    'django_extensions',
)

# Userena settings
LOGIN_REDIRECT_URL = '/accounts/%(username)s/'
LOGIN_URL = '/accounts/signin/'
LOGOUT_URL = '/accounts/signout/'
AUTH_PROFILE_MODULE = 'profiles.Profile'

USERENA_DISABLE_PROFILE_LIST = True
USERENA_MUGSHOT_SIZE = 140

# Test settings
TEST_RUNNER = 'django.test.simple.DjangoTestSuiteRunner'
SOUTH_TESTS_MIGRATE = False

# Guardian
ANONYMOUS_USER_ID = -1
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'admin@cittybox.com'
EMAIL_HOST_PASSWORD = 'asdasd123123'
EMAIL_PORT = 587

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
