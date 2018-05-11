# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_article'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='reqirement',
            new_name='requirement',
        ),
    ]
