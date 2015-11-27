# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0018_dateoptions'),
    ]

    operations = [
        migrations.CreateModel(
            name='TextOptions',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Předmět')),
                ('identifier', models.CharField(max_length=200, verbose_name='Identifikator')),
                ('text', models.CharField(max_length=200, verbose_name='Text')),
            ],
            options={
                'verbose_name_plural': 'Nastavení - Texty',
                'verbose_name': 'Nastavení - Text',
            },
        ),
    ]
