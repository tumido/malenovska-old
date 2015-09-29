#!/usr/bin/env python

from setuptools import setup

setup(
    # GETTING-STARTED: set your app name:
    name='Malenovska webpages',
    # GETTING-STARTED: set your app version:
    version='1.0',
    # GETTING-STARTED: set your app description:
    description='OpenShift App for www.malenovska.cz web site',
    # GETTING-STARTED: set author name (your name):
    author='Tomas Coufal',
    # GETTING-STARTED: set author email (your email):
    author_email='coufal.tom@gmail.com',
    # GETTING-STARTED: set author url (your url):
    url='http://www.python.org/sigs/distutils-sig/',
    # GETTING-STARTED: define required django version:
    install_requires=['Django<=1.8', 'django-wysiwyg-redactor<=0.4.9', 'virtualenv<=13.1.2', 'openpyxl<=2.2.6', 'Pillow<=2.8.2'],
)
