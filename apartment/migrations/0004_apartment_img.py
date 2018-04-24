# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apartment', '0003_auto_20180413_1505'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartment',
            name='img',
            field=models.ImageField(default='', upload_to=''),
            preserve_default=False,
        ),
    ]
