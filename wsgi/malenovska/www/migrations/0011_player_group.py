# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0010_race_fraction'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='group',
            field=models.CharField(default='', max_length=200, verbose_name='Skupina'),
            preserve_default=False,
        ),
    ]
