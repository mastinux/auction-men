# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bidplacing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuctionUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='bid',
            name='bidder',
            field=models.ForeignKey(to='bidplacing.AuctionUser'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='product_name',
            field=models.OneToOneField(to='bidplacing.Product'),
        ),
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.CharField(unique=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='seller',
            field=models.ForeignKey(to='bidplacing.AuctionUser'),
        ),
    ]
