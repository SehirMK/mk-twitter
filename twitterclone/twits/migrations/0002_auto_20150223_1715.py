# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('twits', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='twit',
            name='fav_count',
            field=models.IntegerField(default=0, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='twit',
            name='fav_users',
            field=models.ManyToManyField(related_name='fav_users', null=True, to=settings.AUTH_USER_MODEL, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='twit',
            name='rt_count',
            field=models.IntegerField(default=0, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='twit',
            name='rt_users',
            field=models.ManyToManyField(related_name='rt_users', null=True, to=settings.AUTH_USER_MODEL, blank=True),
            preserve_default=True,
        ),
    ]
