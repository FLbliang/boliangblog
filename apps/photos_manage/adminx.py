# -*- coding: utf-8 -*-
# author: 'boliang'
# date: 2017/10/22 16:35


import xadmin
from xadmin import views

from .models import PhotoShowRecord


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSetting(object):
    site_title = '博良的BLOG'
    site_footer = '博良的BLOG'
    menu_style = 'accordion'


class PhotoShowRecordAdmin(object):
    list_per_page = 10
    list_display = ['image_type', 'image', 'add_time']
    search_fields = ['image_type', 'image']
    list_filter = ['image_type', 'image', 'add_time']


xadmin.site.register(PhotoShowRecord, PhotoShowRecordAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)



