# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customAuth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=20)),
                ('rent_type', models.BooleanField()),
                ('size', models.FloatField()),
                ('room', models.SmallIntegerField(default=1)),
                ('hall', models.SmallIntegerField(default=0)),
                ('bathroom', models.SmallIntegerField(default=0)),
                ('floor', models.SmallIntegerField()),
                ('has_furniture', models.BooleanField(default=0)),
                ('decoration_type', models.SmallIntegerField()),
                ('price', models.IntegerField()),
                ('payment_type', models.SmallIntegerField()),
                ('forward', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Garden',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('company', models.CharField(max_length=30)),
                ('location_id', models.ForeignKey(db_column='location_id', to='customAuth.Location')),
            ],
        ),
        migrations.CreateModel(
            name='Subway',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('line', models.SmallIntegerField()),
                ('station', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'subway',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('tag', models.CharField(max_length=20)),
                ('apartment_id', models.ForeignKey(to='apartment.Apartment')),
            ],
        ),
        migrations.AddField(
            model_name='apartment',
            name='garden_id',
            field=models.ForeignKey(db_column='garden_id', to='apartment.Garden'),
        ),
        migrations.AddField(
            model_name='apartment',
            name='user_id',
            field=models.ForeignKey(db_column='user_id', to=settings.AUTH_USER_MODEL),
        ),
    ]
