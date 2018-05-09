# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_buyorder_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyorder',
            name='order_date',
            field=models.CharField(max_length=100),
        ),
    ]
