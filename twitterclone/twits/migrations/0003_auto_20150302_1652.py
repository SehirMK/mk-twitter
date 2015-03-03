# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('twits', '0002_auto_20150223_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='follower_following',
            name='followers',
            field=models.ManyToManyField(related_name='followers', null=True, to=settings.AUTH_USER_MODEL, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='follower_following',
            name='following',
            field=models.ManyToManyField(related_name='following', null=True, to=settings.AUTH_USER_MODEL, blank=True),
            preserve_default=True,
        ),
    ]
