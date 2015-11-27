# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0009_auto_20150927_1442'),
    ]

    operations = [
        migrations.AddField(
            model_name='race',
            name='fraction',
            field=models.PositiveSmallIntegerField(verbose_name='Frakce', default=1),
            preserve_default=False,
        ),
    ]
