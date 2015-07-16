# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bidplacing', '0007_auto_20150716_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='product_name',
            field=models.ForeignKey(to='bidplacing.Product'),
        ),
    ]
