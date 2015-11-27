# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0019_textoptions'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='email',
            field=models.CharField(blank=True, verbose_name='E-mail', max_length=200, null=True),
        ),
    ]
