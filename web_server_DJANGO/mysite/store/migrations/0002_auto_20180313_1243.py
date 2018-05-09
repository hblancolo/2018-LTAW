# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_type',
            field=models.CharField(max_length=2, default='No Product', choices=[('BC', 'Bicycle'), ('BK', 'Book'), ('CD', 'CD')]),
        ),
    ]
