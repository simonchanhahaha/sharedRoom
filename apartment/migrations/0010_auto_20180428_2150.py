# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apartment', '0009_auto_20180427_2320'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='garden',
            name='description',
        ),
        migrations.AddField(
            model_name='apartment',
            name='description',
            field=models.TextField(default='hahaha'),
            preserve_default=False,
        ),
    ]
