# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals
from datetime import datetime
from django.db import models
from DjangoUeditor.models import UEditorField


class ArticleSortRecord(models.Model):
    name = models.CharField(max_length=100, verbose_name=u'文章类型名')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    def __unicode__(self):
        return self.name


    class Meta:
        verbose_name = u'文章类型'
        verbose_name_plural = verbose_name


class ArticlesRecord(models.Model):
    sort = models.ForeignKey(ArticleSortRecord, verbose_name=u'文章所属')
    image = models.ImageField(max_length=100,
                              upload_to='articles_img/%Y/%m',
                              verbose_name=u'文章封面图')
    name = models.CharField(max_length=100, verbose_name=u'文章名')
    desc = models.CharField(max_length=200, verbose_name=u'简要描述')
    content = UEditorField(verbose_name=u'文章内容', height=300, width=600, default='',
                        imagePath='uploads/images/',
                        filePath='uploads/files/')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')
    good_clicks = models.IntegerField(default=0, verbose_name=u'点赞数')
    comment_nums = models.IntegerField(default=0, verbose_name=u'评论数')

    def __unicode__(self):
        return self.name


    class Meta:
        verbose_name = u'文章'
        verbose_name_plural = verbose_name
