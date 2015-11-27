# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0028_auto_20151030_0021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extrafiles',
            name='filefield',
            field=models.FileField(verbose_name='Soubor', upload_to='', blank=True),
        ),
    ]
