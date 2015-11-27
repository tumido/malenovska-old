# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0024_auto_20151002_1416'),
    ]

    operations = [
        migrations.CreateModel(
            name='Harmonogram',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('program', models.CharField(max_length=200, verbose_name='Program')),
                ('time_start', models.TimeField(verbose_name='Čas začátku')),
                ('time_end', models.TimeField(verbose_name='Čas konce')),
            ],
            options={
                'verbose_name_plural': 'Harmonogram',
                'verbose_name': 'Program',
            },
        ),
    ]
