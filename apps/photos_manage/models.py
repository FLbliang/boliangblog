# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals
from datetime import datetime

from django.db import models


class PhotoShowRecord(models.Model):
    image_type = models.CharField(max_length=66,
                                  choices=(('banner', u'轮播图展示'),
                                           ('scenery', u'风景图展示'),
                                           ('photos', u'图片墙展示'),
                                           ('headImg', u'头像')),
                                  default='photos', verbose_name=u'图片类型')
    image = models.ImageField(max_length=100, upload_to='photos/%Y/%m', verbose_name=u'好看的图片')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')


    class Meta:
        verbose_name = u'图片存储'
        verbose_name_plural = verbose_name



