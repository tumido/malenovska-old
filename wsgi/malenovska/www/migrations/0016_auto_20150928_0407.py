# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0015_remove_race_count'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutwidget',
            options={'verbose_name': 'Panely a texty všude možně', 'verbose_name_plural': 'Panely a texty všude možně'},
        ),
        migrations.RemoveField(
            model_name='aboutwidget',
            name='rank',
        ),
        migrations.AddField(
            model_name='aboutwidget',
            name='id',
            field=models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, default=0, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aboutwidget',
            name='identifier',
            field=models.CharField(max_length=200, verbose_name='Identifikator pro stranku', default='ahoj'),
            preserve_default=False,
        ),
    ]
