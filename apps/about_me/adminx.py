# -*- coding: utf-8 -*-
# author: 'boliang'
# date: 2017/10/22 17:19


import xadmin

from .models import AboutMeRecord, WritingsRecord, LinksRecord


class AboutMeRecordAdmin(object):
    list_display = [
        'id', 'name', 'age', 'job',
        'qq', 'github', 'weiblog',
        'hobbies', 'motto', 'image',
        'head_image', 'desc', 'add_time']
    list_per_page = 1


class WritingsRecordAdmin(object):
    list_display = ['type','from_name', 'content', 'add_time']
    search_fields = ['type', 'from_name']
    list_filter = ['type','from_name', 'add_time']
    list_per_page = 10


class LinksRecordAdmin(object):
    list_display = ['name', 'url', 'add_time']
    search_fields = ['name', 'url']
    list_filter = ['name', 'url', 'add_time']
    list_per_page = 10


xadmin.site.register(AboutMeRecord, AboutMeRecordAdmin)
xadmin.site.register(WritingsRecord, WritingsRecordAdmin)
xadmin.site.register(LinksRecord, LinksRecordAdmin)
