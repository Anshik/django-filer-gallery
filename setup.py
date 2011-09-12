from setuptools import setup, find_packages
import os
import filer_gallery

CLASSIFIERS=[
    'Development Status :: 4 - Beta',
    'Environment :: Web Environment',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Framework :: Django'
]

setup(
    name='django-filer-gallery',
    version=filer_gallery.get_version(),
    description='A gallery using django-filer',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
    author='\xc3yvind Saltvik',
    author_email='oyvind.saltvik@gmail.com',
    url='http://github.com/fivethreeo/django-filer-gallery.git',
    packages=find_packages(),
    classifiers = CLASSIFIERS,
    test_suite = "filer_gallery.test.run_tests.run_tests",
    include_package_data=True,
    zip_safe=False,
    install_requires=['django-catecories', 'django-filer']
)