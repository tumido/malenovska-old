Malenovska.cz
=============

The source codes for the webpages you can find in the
`wsgi/malenovska/` folder. Everything else is just a wrapper to facilitate
deploying [Django](https://www.djangoproject.com/) on the
[OpenShift](https://www.openshift.com/).

Requirements
------------

App runs on Python 3 and all necessary packages can be installed via pip.

```
pip install -r requirements.txt
```

For running in production Django is set to run with PostgreSQL database.


Running locally
---------------

For debugging purposes you can run our server locally. Following setup will let
you create your very own SQLite database and launches server at localhost.

```
cd wsgi/malenovska/
python manage.py makemigrations www
python manage.py migrate
python manage.py runserver
```

With this setup you have debugging enabled in Django settings.

Django on OpenShift
-------------------

For more information take a look at [this](https://github.com/openshift/django-example) project on GitHub. There you can find the same platform we've started here with.