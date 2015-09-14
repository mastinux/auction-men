# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bidplacing', '0013_auto_20150909_1459'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='object_type',
            field=models.CharField(default=b'pr', max_length=2, choices=[(b'pr', b'Product'), (b'sr', b'Service')]),
        ),
    ]
