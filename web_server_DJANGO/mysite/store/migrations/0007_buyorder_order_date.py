# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_remove_buyorder_order_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyorder',
            name='order_date',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2018, 4, 8, 0, 49, 8, 831349, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
