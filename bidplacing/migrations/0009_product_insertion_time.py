# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bidplacing', '0008_auto_20150716_1334'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='insertion_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 16, 15, 19, 32, 981809, tzinfo=utc), blank=True),
        ),
    ]
