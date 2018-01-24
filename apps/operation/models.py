# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals
from datetime import datetime
from django.db import models

from articles_manage.models import ArticlesRecord


class SendMessageRecord(models.Model):
    username = models.CharField(max_length=100, verbose_name=u'发送者名字')
    image = models.CharField(max_length=66, verbose_name=u'头像')
    message = models.CharField(max_length=200, verbose_name=u'留言')
    email = models.CharField(max_length=100, verbose_name=u'邮箱', default='')
    address = models.CharField(max_length=200, verbose_name=u'个人网站', default='')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    def __unicode__(self):
        return self.username

    class Meta:
        verbose_name = u'留言信息'
        verbose_name_plural = verbose_name


class SendCommentRecord(models.Model):
    from_article = models.ForeignKey(ArticlesRecord, verbose_name=u'所属文章')
    username = models.CharField(max_length=100, verbose_name=u'发送者名字')
    image = models.CharField(max_length=66, verbose_name=u'头像')
    message = models.CharField(max_length=200, verbose_name=u'留言')
    email = models.CharField(max_length=100, verbose_name=u'邮箱', default='')
    address = models.CharField(max_length=200, verbose_name=u'个人网站', default='')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    def __unicode__(self):
        return self.username

    class Meta:
        verbose_name = u'评论信息'
        verbose_name_plural = verbose_name


