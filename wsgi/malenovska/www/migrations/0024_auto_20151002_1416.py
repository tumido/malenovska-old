# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import redactor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0023_auto_20151001_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='race',
            name='description',
            field=redactor.fields.RedactorField(verbose_name='Popis', blank=True),
        ),
    ]
