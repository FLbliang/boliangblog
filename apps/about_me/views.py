# -*- coding: utf-8 -*-
# author: 'boliang'
# date: 2017/10/22 21:03

from django.shortcuts import render
from django.views.generic import View

from .models import AboutMeRecord
from articles_manage.models import ArticlesRecord


class AboutView(View):
    def get(self, request):

        try:
            about_me = AboutMeRecord.objects.get(id = 1)
        except:
            about_me = None

        articles = ArticlesRecord.objects.order_by('-add_time')[:5]

        return render(request, 'about.html', {
            'active': 'about',
            'about_me': about_me,
            'articles': articles
        })
