# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0007_auto_20150927_0222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='date',
            field=models.DateTimeField(verbose_name='Datum registrace'),
        ),
    ]
