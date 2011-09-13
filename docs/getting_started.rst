Dependencies
------------

* Django >= 1.2.7
* django-filer >= 0.8.3
* easy-thumbnails >= 1.0-alpha-16
* django-staticfiles or django.contrib.staticfiles

Installation
------------

Install `django-filer-gallery` from github and `easy-thumbnails` using pip: ::

    pip install -e http://github.com/fivethreeo/django-filer-gallery.git#egg=django-filer-gallery
    pip install easy-thumbnails==1.0-alpha-16

Add the required apps to ``INSTALLED_APPS``::

    INSTALLED_APPS = (
        ...
        'filer_gallery',
        'easy_thumbnails',
        'filer',
        'django.contrib.staticfiles',
        # 'staticfiles'
        ...
    )

and then run ``syncdb`` or ``migrate`` if you're using South.