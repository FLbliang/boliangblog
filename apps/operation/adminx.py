# -*- coding: utf-8 -*-
# author: 'boliang'
# date: 2017/10/22 19:43


import xadmin

from .models import SendMessageRecord, SendCommentRecord


class SendMessageRecordAdmin(object):
    list_display = ['username', 'image', 'message', 'email', 'address', 'add_time']
    search_fields = ['username', 'image', 'email', 'address']
    list_filter = ['username', 'image','email','address', 'add_time']
    list_per_page = 10


class SendCommentRecordAdmin(object):
    list_display = ['from_article', 'username', 'image', 'message','email','address', 'add_time']
    search_fields = ['from_article', 'username', 'image', 'email', 'address']
    list_filter = ['from_article', 'username', 'image', 'email','address', 'add_time']
    list_per_page = 10


xadmin.site.register(SendMessageRecord, SendMessageRecordAdmin)
xadmin.site.register(SendCommentRecord, SendCommentRecordAdmin)