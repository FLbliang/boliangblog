# -*- coding: utf-8 -*-
# author: 'boliang'
# date: 2017/10/24 11:58


from django.conf.urls import url

from .views import IndexView, Ie8View


urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'ie8_error', Ie8View.as_view(), name='ie8')
]