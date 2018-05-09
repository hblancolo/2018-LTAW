# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('product_type', models.CharField(max_length=100)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('product_price', models.FloatField()),
                ('product_specs', models.CharField(max_length=500)),
                ('product_pics', models.FileField(upload_to='')),
                ('product_multimedia', models.FileField(upload_to='', blank=True)),
            ],
        ),
    ]
