# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0003_auto_20150926_2131'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='legend',
            name='race',
        ),
        migrations.AddField(
            model_name='legend',
            name='race',
            field=models.ForeignKey(to='www.Race', default=''),
            preserve_default=False,
        ),
    ]
