# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0021_mappoints'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='email',
            field=models.EmailField(blank=True, max_length=200, verbose_name='E-mail', null=True),
        ),
        migrations.AlterField(
            model_name='race',
            name='icon',
            field=models.ImageField(blank=True, upload_to='race_img/', verbose_name='Obrázek'),
        ),
    ]
