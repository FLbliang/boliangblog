# -*- coding: utf-8 -*-
# author: 'boliang'
# date: 2017/10/23 22:27


from django.conf.urls import url

from .views import PhotoShowView


urlpatterns = [
    url(r'^$', PhotoShowView.as_view(), name='photos')
]