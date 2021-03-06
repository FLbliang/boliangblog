# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-10-23 15:27
from __future__ import unicode_literals

import DjangoUeditor.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles_manage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlesrecord',
            name='desc',
            field=models.CharField(default=1, max_length=200, verbose_name='\u7b80\u8981\u63cf\u8ff0'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='articlesrecord',
            name='content',
            field=DjangoUeditor.models.UEditorField(default='', verbose_name='\u6587\u7ae0\u5185\u5bb9'),
        ),
    ]
