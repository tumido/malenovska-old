# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0011_player_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='race',
            name='limit',
            field=models.PositiveSmallIntegerField(verbose_name='Max. hráčů', default=30),
            preserve_default=False,
        ),
    ]
