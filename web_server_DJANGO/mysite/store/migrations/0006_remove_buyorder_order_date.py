# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20180408_0026'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buyorder',
            name='order_date',
        ),
    ]
