# -*- coding: utf-8 -*-
# author: 'boliang'
# date: 2017/10/22 22:21


from django.conf.urls import url

from .views import MessageView, SendCommentView, SendGoodclicksView


urlpatterns = [
    url(r'^$', MessageView.as_view(), name='message'),
    url(r'^send_message/$', MessageView.as_view(), name='send_message'),
    url(r'^send_comment/$', SendCommentView.as_view(), name='send_comment'),
    url(r'^send_good_clicks/$', SendGoodclicksView.as_view(), name='send_good_clicks')
]

