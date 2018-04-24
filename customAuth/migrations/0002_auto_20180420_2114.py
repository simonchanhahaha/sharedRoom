# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customAuth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='avatar',
            name='img',
            field=models.ImageField(default='', upload_to='avatar'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='avatar',
            name='path',
            field=models.CharField(max_length=40),
        ),
    ]
