# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0026_auto_20151016_2057'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtraFiles',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200, verbose_name='Jméno')),
                ('filefield', models.FileField(verbose_name='Soubor', upload_to='')),
            ],
            options={
                'verbose_name': 'Soubor',
                'verbose_name_plural': 'Nahrané soubory',
            },
        ),
    ]
