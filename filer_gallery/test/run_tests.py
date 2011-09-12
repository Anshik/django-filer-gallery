# -*- coding: utf-8 -*-
import sys
import django

INSTALLED_APPS=[
    'filer_gallery.test.testapp',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.sites',        
    'filer_gallery'
]

MIDDLEWARE_CLASSES = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.contrib.csrf.middleware.CsrfViewMiddleware'
]

TEMPLATE_CONTEXT_PROCESSORS = [
    "django.core.context_processors.auth",
    "django.core.context_processors.i18n",
    "django.core.context_processors.debug",
    "django.core.context_processors.request",
    "django.core.context_processors.media"
]

if django.VERSION[1] < 3: # pragma: no cover
    MIDDLEWARE_CLASSES.insert(6, 'cbv.middleware.DeferredRenderingMiddleware')
    INSTALLED_APPS.append('staticfiles')
    INSTALLED_APPS.append('cbv')
    TEMPLATE_CONTEXT_PROCESSORS.append('staticfiles.context_processors.static')
else:
    INSTALLED_APPS.append('django.contrib.staticfiles')
    TEMPLATE_CONTEXT_PROCESSORS.append('django.core.context_processors.static')
    
def run_tests():
    
    from django.conf import settings
    
    settings.configure(
        INSTALLED_APPS = INSTALLED_APPS,
        MIDDLEWARE_CLASSES = MIDDLEWARE_CLASSES,
        TEMPLATE_CONTEXT_PROCESSORS = TEMPLATE_CONTEXT_PROCESSORS,
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': 'filer_gallery_tests.db',
            }
        },
        ROOT_URLCONF='filer_gallery.test.testapp.urls',
        LANGUAGES=(('en', 'English'),('de','German'),('nb','Norwegian'),('nn','Norwegian Nynorsk')),
        STATIC_URL='/some/url/',
        TEST_RUNNER = 'xmlrunner.extra.djangotestrunner.XMLTestRunner',
        TEST_OUTPUT_VERBOSE = True
    )
    
    from django.test.utils import get_runner

    failures = get_runner(settings)().run_tests(['filer_gallery'])
    sys.exit(failures)

if __name__ == '__main__':
    run_tests()