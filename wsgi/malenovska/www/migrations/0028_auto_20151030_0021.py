# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0027_extrafiles'),
    ]

    operations = [
        migrations.AddField(
            model_name='extrafiles',
            name='tooltip',
            field=models.CharField(max_length=200, verbose_name='Popisek', default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='extrafiles',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Titulek'),
        ),
    ]
