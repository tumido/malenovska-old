# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0016_auto_20150928_0407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='nick',
            field=models.CharField(verbose_name='Přezdívka', null=True, blank=True, max_length=200),
        ),
    ]
