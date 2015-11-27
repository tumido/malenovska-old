# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0004_auto_20150926_2133'),
    ]

    operations = [
        migrations.AddField(
            model_name='race',
            name='active',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
