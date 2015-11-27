# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0013_race_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='group',
            field=models.CharField(null=True, verbose_name='Skupina', blank=True, max_length=200),
        ),
    ]
