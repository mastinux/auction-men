# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('bidplacing', '0005_auto_20150701_1633'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.AlterField(
            model_name='auctionsuser',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, unique=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(default=None, blank=True, to='bidplacing.Category', null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(max_length=500, blank=True),
        ),
        migrations.AddField(
            model_name='image',
            name='product_name',
            field=models.ForeignKey(to='bidplacing.Product'),
        ),
    ]
