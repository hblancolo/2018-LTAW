# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_product_product_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='buyOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('product_name', models.CharField(max_length=100)),
                ('order_date', models.DateTimeField(auto_now=True)),
                ('shipping_address', models.CharField(max_length=300)),
                ('zip_code', models.IntegerField(max_length=5)),
                ('country', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='product_pics',
            field=models.FileField(upload_to='', blank=True),
        ),
    ]
