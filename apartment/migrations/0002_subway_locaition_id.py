# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customAuth', '0001_initial'),
        ('apartment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subway',
            name='locaition_id',
            field=models.ForeignKey(default=1, db_column='location_id', to='customAuth.Location'),
            preserve_default=False,
        ),
    ]
