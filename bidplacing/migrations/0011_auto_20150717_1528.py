# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bidplacing', '0010_auto_20150716_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='bidding_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
