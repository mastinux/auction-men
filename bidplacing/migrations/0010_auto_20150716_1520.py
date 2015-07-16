# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bidplacing', '0009_product_insertion_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='insertion_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
