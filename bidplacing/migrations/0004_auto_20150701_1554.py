# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bidplacing', '0003_auto_20150701_1542'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AuctionUser',
            new_name='AuctionsUser',
        ),
    ]
