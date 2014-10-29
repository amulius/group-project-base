# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slides', '0002_auto_20141026_1826'),
    ]

    operations = [
        migrations.AddField(
            model_name='done',
            name='slide',
            field=models.ForeignKey(related_name='is_done', blank=True, to='slides.Slide', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='help',
            name='slide',
            field=models.ForeignKey(related_name='needs_help', blank=True, to='slides.Slide', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='question',
            name='slide',
            field=models.ForeignKey(related_name='questions', blank=True, to='slides.Slide', null=True),
            preserve_default=True,
        ),
    ]
