# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('apartment', '0004_apartment_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartment',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 21, 13, 27, 38, 736909, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='apartment',
            name='subway_id',
            field=models.ForeignKey(default='', db_column='subway_id', to='apartment.Subway'),
        ),
    ]
