# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apartment', '0005_auto_20180421_2127'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartment',
            name='is_rent',
            field=models.BooleanField(default=0),
        ),
    ]
