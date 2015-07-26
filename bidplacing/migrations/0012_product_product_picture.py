# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bidplacing', '0011_auto_20150717_1528'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_picture',
            field=models.ImageField(default=b'bidplacing/templates/product_media/no-img.jpg', upload_to=b'bidplacing/templates/product_media/'),
        ),
    ]
