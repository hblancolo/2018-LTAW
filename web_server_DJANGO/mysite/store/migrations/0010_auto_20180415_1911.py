# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_auto_20180408_1524'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buyorder',
            name='country',
        ),
        migrations.RemoveField(
            model_name='buyorder',
            name='order_date',
        ),
        migrations.AddField(
            model_name='buyorder',
            name='user_name',
            field=models.CharField(max_length=100, default=datetime.datetime(2018, 4, 15, 17, 11, 13, 3950, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
