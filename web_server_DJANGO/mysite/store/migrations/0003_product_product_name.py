# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20180313_1243'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_name',
            field=models.CharField(default='bisicleta to wapa', max_length=100),
            preserve_default=False,
        ),
    ]
