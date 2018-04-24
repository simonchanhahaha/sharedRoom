# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apartment', '0006_apartment_is_rent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apartment',
            name='subway_id',
        ),
    ]
