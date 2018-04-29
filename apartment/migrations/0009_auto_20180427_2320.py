# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import apartment.models


class Migration(migrations.Migration):

    dependencies = [
        ('apartment', '0008_auto_20180424_2053'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApartmentImg',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('img', models.ImageField(upload_to=apartment.models.apartment_img_path)),
            ],
        ),
        migrations.RemoveField(
            model_name='apartment',
            name='img',
        ),
        migrations.AddField(
            model_name='apartmentimg',
            name='apartment',
            field=models.ForeignKey(to='apartment.Apartment'),
        ),
    ]
