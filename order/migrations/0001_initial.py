# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('apartment', '0012_apartment_views'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.CharField(primary_key=True, max_length=20, serialize=False)),
                ('is_check', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('apartment', models.ForeignKey(to='apartment.Apartment')),
                ('consumer', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Star',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('apartment', models.ForeignKey(db_column='apartment_id', to='apartment.Apartment')),
                ('user', models.ForeignKey(db_column='user_id', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
