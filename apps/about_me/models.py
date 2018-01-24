# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals
from datetime import datetime

from django.db import models


class AboutMeRecord(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name=u'我的名字')
    age = models.IntegerField(default=21, verbose_name=u'年龄')
    job = models.CharField(max_length=100, verbose_name=u'职业')
    qq = models.CharField(max_length=100, default='971791872', verbose_name=u'QQ号码')
    github = models.CharField(
        max_length=100,
        default='https://www.github.com',
        verbose_name='github账号')
    weiblog = models.CharField(
        max_length=100,
        default='https://www.weibo.com',
        verbose_name=u'微博账号')
    hobbies = models.CharField(max_length=200, default='Code Tour', verbose_name=u'爱好')
    motto = models.CharField(max_length=200, default=u'想法丰富多彩离不开执行力', verbose_name=u'格言')
    image = models.ImageField(max_length=100, upload_to='about_me/%Y/%m', verbose_name=u'我的照片')
    head_image = models.ImageField(max_length=100, upload_to='about_me/%Y/%m', verbose_name=u'我的头像')
    desc = models.TextField(verbose_name=u'自我描述')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')


    class Meta:
        verbose_name = u'关于我'
        verbose_name_plural = verbose_name


class WritingsRecord(models.Model):
    type = models.CharField(max_length=20,
                            choices=(('from_me', u'随笔吹水'),
                                     ('from_others', u'名人名言')),
                            default='from_me',
                            verbose_name=u'类型')
    from_name = models.CharField(max_length=66, default='', verbose_name=u'是谁')
    content = models.CharField(max_length=200, verbose_name=u'内容')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')


    class Meta:
        verbose_name = u'写一写'
        verbose_name_plural = verbose_name


class LinksRecord(models.Model):
    name = models.CharField(max_length=20, verbose_name=u'链接名字')
    url = models.CharField(max_length=200, verbose_name=u'链接url')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')


    class Meta:
        verbose_name = u'常用链接'
        verbose_name_plural = verbose_name













