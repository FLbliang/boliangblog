# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-10-25 08:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about_me', '0003_writingsrecord_from_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutmerecord',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]