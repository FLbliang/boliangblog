# -*- coding: utf-8 -*-
# author: 'boliang'
# date: 2017/10/22 17:48


import xadmin

from .models import ArticleSortRecord, ArticlesRecord


class ArticleSortRecordAdmin(object):
    list_display = ['name', 'add_time']
    search_fields = ['name']
    list_filter = ['name', 'add_time']
    list_per_page = 10


class ArticlesRecordAdmin(object):
    list_display = ['sort', 'name', 'desc', 'good_clicks', 'comment_nums', 'add_time']
    search_fields = ['sort', 'name', 'good_clicks', 'comment_nums']
    list_filter = ['sort', 'name', 'good_clicks', 'comment_nums', 'add_time']
    style_fields = {'content' : 'ueditor'}
    list_per_page = 10


xadmin.site.register(ArticleSortRecord, ArticleSortRecordAdmin)
xadmin.site.register(ArticlesRecord, ArticlesRecordAdmin)