# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0025_harmonogram'),
    ]

    operations = [
        migrations.AlterField(
            model_name='harmonogram',
            name='time_end',
            field=models.TimeField(blank=True, null=True, verbose_name='Čas konce'),
        ),
    ]
