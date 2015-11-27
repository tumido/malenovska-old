# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0008_auto_20150927_0225'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='player',
            unique_together=set([('name', 'surname', 'nick')]),
        ),
    ]
