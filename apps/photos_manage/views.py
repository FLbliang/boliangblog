# -*- coding: utf-8 -*-
# author: 'boliang'
# date: 2017/10/23 22:27

from django.shortcuts import render
from django.views.generic import View

from .models import PhotoShowRecord
from utils.util import Util
from utils.util import random

class PhotoShowView(View):
    def get(self, request):
        util = Util()
        photo_shows = PhotoShowRecord.objects.filter(image_type='photos')
        try:
            photo_shows = util.selectData(
                datas = photo_shows,
                data_len = photo_shows.count(),
                select_len = 12
            )

            colors = ['shadow-blue', 'shadow-yellow', 'shadow-orangered', 'shadow-red', 'shadow-green']

            tmp_photo_shows = []
            for photo_show in photo_shows:
                index = random.randint(0, 4)
                photo_show = {
                    'photo_show': photo_show,
                    'color': colors[index]
                }
                tmp_photo_shows.append(photo_show)
        except:
            tmp_photo_shows = None

        return render(request, 'photos.html', {
            'tmp_photo_shows': tmp_photo_shows,
            'active': 'photos',
        })


