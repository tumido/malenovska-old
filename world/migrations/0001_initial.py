# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-24 17:15
from __future__ import unicode_literals

from django.db import migrations, models
import redactor.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Jméno rasy')),
                ('description', redactor.fields.RedactorField(blank=True, verbose_name='Popis')),
                ('icon', models.ImageField(blank=True, upload_to='race_img/', verbose_name='Obrázek')),
                ('active', models.BooleanField(verbose_name='Letos bojuje')),
                ('fraction', models.PositiveSmallIntegerField(verbose_name='Frakce')),
                ('limit', models.PositiveSmallIntegerField(verbose_name='Max. hráčů')),
            ],
            options={
                'verbose_name': 'Rasa',
                'verbose_name_plural': 'Rasy',
            },
        ),
    ]