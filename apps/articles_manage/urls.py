# -*- coding: utf-8 -*-
# author: 'boliang'
# date: 2017/10/23 22:57


from django.conf.urls import url

from .views import FeelingsView, StudyView, ArticlesView

urlpatterns = [
    url(r'^feelings/', FeelingsView.as_view(), name='feelings'),
    url(r'^study/', StudyView.as_view(), name='study'),
    url(r'^article/', ArticlesView.as_view(), name='article')
]
