# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customAuth', '0003_auto_20180427_1756'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='location',
            table='Location',
        ),
    ]
