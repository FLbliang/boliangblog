# -*- coding: utf-8 -*-
# author: 'boliang'
# date: 2017/10/22 21:03


from django.conf.urls import url

from .views import AboutView


urlpatterns = [
    url(r'^$', AboutView.as_view(), name='about')
]