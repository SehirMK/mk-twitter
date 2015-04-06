# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Follower_Following',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('followers', models.ManyToManyField(related_name='followers', null=True, to=settings.AUTH_USER_MODEL, blank=True)),
                ('following', models.ManyToManyField(related_name='following', null=True, to=settings.AUTH_USER_MODEL, blank=True)),
                ('user', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OwnedTwit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RTedTwit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Twit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField(max_length=140)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('timestamp2', models.DateTimeField(auto_now_add=True)),
                ('fav_count', models.IntegerField(default=0, null=True, blank=True)),
                ('rt_count', models.IntegerField(default=0, null=True, blank=True)),
                ('fav_users', models.ManyToManyField(related_name='fav_users', null=True, to=settings.AUTH_USER_MODEL, blank=True)),
                ('mainuser', models.ForeignKey(related_name='mainuser', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('rt_users', models.ManyToManyField(related_name='rt_users', null=True, to=settings.AUTH_USER_MODEL, blank=True)),
                ('user', models.ForeignKey(related_name='user', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Twits',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('twit_type_id', models.PositiveIntegerField()),
                ('twit_type_name', models.ForeignKey(to='contenttypes.ContentType')),
                ('user', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='rtedtwit',
            name='twit',
            field=models.ForeignKey(blank=True, to='twits.Twit', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='rtedtwit',
            name='user',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ownedtwit',
            name='twit',
            field=models.ForeignKey(blank=True, to='twits.Twit', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ownedtwit',
            name='user',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]
