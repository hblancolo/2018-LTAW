# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20180405_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyorder',
            name='zip_code',
            field=models.IntegerField(),
        ),
    ]
