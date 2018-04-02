# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(verbose_name='last login', blank=True, null=True)),
                ('username', models.CharField(verbose_name='Username', max_length=20, unique=True)),
                ('email', models.EmailField(verbose_name='Email', max_length=254, unique=True)),
                ('is_staff', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('province', models.CharField(max_length=20)),
                ('pid', models.ForeignKey(blank=True, null=True, db_column='pid', to='customAuth.Location')),
            ],
        ),
        # migrations.CreateModel(
        #     name='Users_profile',
        #     fields=[
        #         ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
        #         ('gender', models.BooleanField(default=0)),
        #         ('phone', models.CharField(max_length=11)),
        #         ('wechat', models.CharField(max_length=20)),
        #         ('location', models.ForeignKey(to='customAuth.Location')),
        #     ],
        # ),
    ]
