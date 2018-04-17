# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apartment', '0002_subway_locaition_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subway',
            name='line',
            field=models.CharField(max_length=10),
        ),
    ]
