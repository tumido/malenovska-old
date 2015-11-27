# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0020_player_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='MapPoints',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='Název', max_length=200)),
                ('long', models.CharField(verbose_name='Zeměpisná délka', max_length=200)),
                ('lat', models.CharField(verbose_name='Zeměpisná šířka', max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Nastavení - Mapa',
                'verbose_name': 'Bod na mapě',
            },
        ),
    ]
