# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apartment', '0011_auto_20180429_1648'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartment',
            name='views',
            field=models.IntegerField(default=1),
        ),
    ]
