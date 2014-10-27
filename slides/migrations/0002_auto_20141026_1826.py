# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('slides', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Done',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('student', models.ForeignKey(related_name='is_done', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Help',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('helped', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('student', models.ForeignKey(related_name='needs_help', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('answered', models.BooleanField(default=False)),
                ('text', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('student', models.ForeignKey(related_name='questions', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=40)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='person',
            name='image',
            field=models.ImageField(default=b'profile_image/default.png', null=True, upload_to=b'profile_image', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='person',
            name='is_student',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
