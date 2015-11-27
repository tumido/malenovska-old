# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0002_auto_20150926_2129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='race',
            name='icon',
            field=models.ImageField(upload_to='', blank=True),
        ),
    ]
