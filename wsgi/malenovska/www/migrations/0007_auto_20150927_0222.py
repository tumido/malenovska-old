# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import redactor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0006_auto_20150926_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutwidget',
            name='text',
            field=redactor.fields.RedactorField(),
        ),
        migrations.AlterField(
            model_name='legend',
            name='text',
            field=redactor.fields.RedactorField(),
        ),
        migrations.AlterField(
            model_name='news',
            name='text',
            field=redactor.fields.RedactorField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='date',
            field=models.DateTimeField(verbose_name='Datum registrace', null=True),
        ),
        migrations.AlterField(
            model_name='race',
            name='description',
            field=redactor.fields.RedactorField(verbose_name='Popis'),
        ),
    ]
