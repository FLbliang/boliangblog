# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-10-25 02:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0002_auto_20171024_2324'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sendcommentrecord',
            old_name='comment',
            new_name='message',
        ),
    ]