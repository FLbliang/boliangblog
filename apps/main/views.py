# -*- coding: utf-8 -*-
# author: 'boliang'
# date: 2017/10/24 11:54


from django.shortcuts import render
from django.views.generic import View

from photos_manage.models import PhotoShowRecord
from articles_manage.models import ArticlesRecord
from about_me.models import AboutMeRecord, WritingsRecord, LinksRecord
from utils.util import Util


class IndexView(View):
    def get(self, request):
        util = Util()
        photo_shows = PhotoShowRecord.objects.filter(image_type='banner')
        photo_shows = util.selectData(
            datas = photo_shows,
            data_len = photo_shows.count(),
            select_len = 5
        )

        writing_image = PhotoShowRecord.objects.filter(image_type='scenery')

        try:
            writing_image = util.selectData(
                datas = writing_image,
                data_len = writing_image.count(),
                select_len = 1
            )[0]
        except:
            writing_image = None


        articles = ArticlesRecord.objects.order_by('-add_time')[:5]

        try:
            about_me = AboutMeRecord.objects.get(id=1)
        except:
            about_me = None

        try:
            writing = WritingsRecord.objects.filter(type='from_me')
            writing = writing.order_by('-add_time')[0]
        except:
            writing = None

        links = LinksRecord.objects.all()

        return render(request, 'index.html', {
            'active': 'home',
            'photo_shows': photo_shows,
            'articles': articles,
            'about_me': about_me,
            'writing': writing,
            'links': links,
            'writing_image': writing_image

        })


class Ie8View(View):
    def get(self, request):
        return render(request, 'ie8.html')