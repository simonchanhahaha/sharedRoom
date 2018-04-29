# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apartment', '0010_auto_20180428_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='name',
            field=models.CharField(max_length=40),
        ),
    ]
