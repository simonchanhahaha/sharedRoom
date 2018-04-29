# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import customAuth.models


class Migration(migrations.Migration):

    dependencies = [
        ('customAuth', '0002_auto_20180420_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avatar',
            name='img',
            field=models.ImageField(upload_to=customAuth.models.avatar_path),
        ),
    ]
