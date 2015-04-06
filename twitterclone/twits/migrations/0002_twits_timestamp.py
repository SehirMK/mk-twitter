# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('twits', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='twits',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 6, 17, 37, 3, 295087), auto_now_add=True),
            preserve_default=False,
        ),
    ]
