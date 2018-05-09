# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_auto_20180408_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyorder',
            name='order_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
