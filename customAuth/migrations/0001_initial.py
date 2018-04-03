# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Avatar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('path', models.ImageField(upload_to='avatar')),
                ('version', models.SmallIntegerField(default=1)),
                ('user_id', models.OneToOneField(db_column='user_id', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('province', models.CharField(max_length=20)),
                ('pid', models.ForeignKey(blank=True, null=True, db_column='pid', to='customAuth.Location')),
            ],
        ),
        migrations.CreateModel(
            name='Users_profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('gender', models.BooleanField(default=0)),
                ('phone', models.CharField(max_length=11)),
                ('wechat', models.CharField(max_length=20, blank=True, null=True)),
                ('location', models.ForeignKey(db_column='location_id', to='customAuth.Location')),
                ('user_id', models.OneToOneField(db_column='user_id', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
