# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('bidplacing', '0006_auto_20150704_1026'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auctionsuser',
            name='user',
        ),
        migrations.RemoveField(
            model_name='image',
            name='product_name',
        ),
        migrations.AlterField(
            model_name='bid',
            name='bidder',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='bid',
            name='product_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.CharField(unique=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='product',
            name='seller',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='AuctionsUser',
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]
