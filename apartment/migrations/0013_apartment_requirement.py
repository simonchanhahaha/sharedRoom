# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apartment', '0012_apartment_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartment',
            name='requirement',
            field=models.CharField(max_length=20, blank=True, null=True),
        ),
    ]
