# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0017_auto_20150928_1451'),
    ]

    operations = [
        migrations.CreateModel(
            name='DateOptions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='Událost', max_length=200)),
                ('identifier', models.CharField(verbose_name='Identifikator', max_length=200)),
                ('date', models.DateTimeField(verbose_name='Datum')),
            ],
            options={
                'verbose_name': 'Nastavení - Datum',
                'verbose_name_plural': 'Nastavení - Data',
            },
        ),
    ]
