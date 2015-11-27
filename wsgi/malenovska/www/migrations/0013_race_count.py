# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0012_race_limit'),
    ]

    operations = [
        migrations.AddField(
            model_name='race',
            name='count',
            field=models.PositiveSmallIntegerField(verbose_name='Počet hráčů', default=0),
        ),
    ]
