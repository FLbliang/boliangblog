# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-10-22 11:16
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutMeRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='\u6211\u7684\u540d\u5b57')),
                ('age', models.IntegerField(default=21, verbose_name='\u5e74\u9f84')),
                ('job', models.CharField(max_length=100, verbose_name='\u804c\u4e1a')),
                ('qq', models.CharField(default='971791872', max_length=100, verbose_name='QQ\u53f7\u7801')),
                ('github', models.CharField(default='https://www.github.com', max_length=100, verbose_name='github\u8d26\u53f7')),
                ('weiblog', models.CharField(default='https://www.weibo.com', max_length=100, verbose_name='\u5fae\u535a\u8d26\u53f7')),
                ('hobbies', models.CharField(default='Code Tour', max_length=200, verbose_name='\u7231\u597d')),
                ('motto', models.CharField(default='\u60f3\u6cd5\u4e30\u5bcc\u591a\u5f69\u79bb\u4e0d\u5f00\u6267\u884c\u529b', max_length=200, verbose_name='\u683c\u8a00')),
                ('image', models.ImageField(upload_to='about_me/%Y/%m', verbose_name='\u6211\u7684\u7167\u7247')),
                ('desc', models.TextField(verbose_name='\u81ea\u6211\u63cf\u8ff0')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u5173\u4e8e\u6211',
                'verbose_name_plural': '\u5173\u4e8e\u6211',
            },
        ),
        migrations.CreateModel(
            name='LinksRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='\u94fe\u63a5\u540d\u5b57')),
                ('url', models.CharField(max_length=200, verbose_name='\u94fe\u63a5url')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u5e38\u7528\u94fe\u63a5',
                'verbose_name_plural': '\u5e38\u7528\u94fe\u63a5',
            },
        ),
        migrations.CreateModel(
            name='WritingsRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('from_me', '\u968f\u7b14\u5439\u6c34'), ('from_others', '\u540d\u4eba\u540d\u8a00')], default='from_me', max_length=20, verbose_name='\u7c7b\u578b')),
                ('content', models.CharField(max_length=200, verbose_name='\u5185\u5bb9')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u5199\u4e00\u5199',
                'verbose_name_plural': '\u5199\u4e00\u5199',
            },
        ),
    ]
