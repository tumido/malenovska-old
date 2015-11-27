# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0005_race_active'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutwidget',
            options={'verbose_name_plural': 'Sekce "Kontakty" apod.', 'verbose_name': 'Panel v "Kontakty" etc.'},
        ),
        migrations.AlterModelOptions(
            name='legend',
            options={'verbose_name_plural': 'Legendy', 'verbose_name': 'Legenda'},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name_plural': 'Novinky', 'verbose_name': 'Novinka'},
        ),
        migrations.AlterModelOptions(
            name='player',
            options={'verbose_name_plural': 'Registrovaní hráči', 'verbose_name': 'Ragistrovaný hráč'},
        ),
        migrations.AlterModelOptions(
            name='race',
            options={'verbose_name_plural': 'Rasy', 'verbose_name': 'Rasa'},
        ),
        migrations.RemoveField(
            model_name='aboutwidget',
            name='id',
        ),
        migrations.AddField(
            model_name='aboutwidget',
            name='rank',
            field=models.PositiveIntegerField(default=0, primary_key=True, serialize=False, verbose_name='Pozice na strance'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='aboutwidget',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Nadpis'),
        ),
        migrations.AlterField(
            model_name='legend',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Název'),
        ),
        migrations.AlterField(
            model_name='legend',
            name='race',
            field=models.ForeignKey(to='www.Race', verbose_name='Týká se rasy'),
        ),
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.DateTimeField(verbose_name='Datum vydání'),
        ),
        migrations.AlterField(
            model_name='news',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Nadpis'),
        ),
        migrations.AlterField(
            model_name='player',
            name='age',
            field=models.PositiveSmallIntegerField(verbose_name='Věk', validators=[django.core.validators.MinValueValidator(10)]),
        ),
        migrations.AlterField(
            model_name='player',
            name='date',
            field=models.DateTimeField(verbose_name='Datum registrace'),
        ),
        migrations.AlterField(
            model_name='player',
            name='ip',
            field=models.GenericIPAddressField(verbose_name='IP adresa'),
        ),
        migrations.AlterField(
            model_name='player',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Jméno'),
        ),
        migrations.AlterField(
            model_name='player',
            name='nick',
            field=models.CharField(max_length=200, verbose_name='Přezdívka'),
        ),
        migrations.AlterField(
            model_name='player',
            name='race',
            field=models.ForeignKey(to='www.Race', verbose_name='Bojuje za'),
        ),
        migrations.AlterField(
            model_name='player',
            name='surname',
            field=models.CharField(max_length=200, verbose_name='Příjmení'),
        ),
        migrations.AlterField(
            model_name='race',
            name='active',
            field=models.BooleanField(verbose_name='Letos bojuje'),
        ),
        migrations.AlterField(
            model_name='race',
            name='description',
            field=models.TextField(verbose_name='Popis'),
        ),
        migrations.AlterField(
            model_name='race',
            name='icon',
            field=models.ImageField(blank=True, upload_to='', verbose_name='Obrázek'),
        ),
        migrations.AlterField(
            model_name='race',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Jméno rasy'),
        ),
    ]
