# -*- coding: utf-8 -*-
# author: 'boliang'
# date: 2017/10/23 22:57

from django.shortcuts import render
from django.views.generic import View
from django.db.models import Q
from pure_pagination import Paginator, PageNotAnInteger
import math

from .models import ArticleSortRecord, ArticlesRecord
from photos_manage.models import PhotoShowRecord
from about_me.models import AboutMeRecord, WritingsRecord
from operation.models import SendCommentRecord
from utils.util import Util, random, IgnorePageOperation


class StudyView(View):
    def get_sort_html(self, request, sort_id):
        article_sort = ArticleSortRecord.objects.get(id=sort_id)
        try:
            about_me = AboutMeRecord.objects.get(id=1)
        except:
            about_me = None
        articles = ArticlesRecord.objects.order_by('-add_time')
        new_articles = articles[:5]
        articles = articles.filter(sort=article_sort)

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(articles, 5, request=request)
        articles = p.page(page)

        return render(request, 'sort.html', {
            'active': 'study',
            'about_me': about_me,
            'article_sort': article_sort,
            'articles': articles,
            'new_articles': new_articles
        })

    def get_total_html(self, request):
        util = Util()
        article_sorts = ArticleSortRecord.objects.all()
        articles = ArticlesRecord.objects.order_by('-add_time')
        try:
            about_me = AboutMeRecord.objects.get(id=1)
        except:
            about_me = None

        new_articles = articles[:5]
        try:
            feelings_sort = article_sorts.get(name='Feelings')
        except:
            feelings_sort = None


        article_sorts = article_sorts.filter(~Q(name = 'Feelings'))
        articles = articles.filter(~Q(sort = feelings_sort))

        colors = ['article-class-btn-color-1',
                  'article-class-btn-color-2',
                  'article-class-btn-color-3',
                  'article-class-btn-color-4']

        article_sorts = util.selectData(
            datas = article_sorts,
            data_len = article_sorts.count(),
            select_len = article_sorts.count()
        )

        tmp_article_sorts = []

        try:
            for article_sort in article_sorts:
                index = random.randint(0, 3)
                tmp_article_sort = {
                    'article_sort': article_sort,
                    'color': colors[index]
                }
                tmp_article_sorts.append(tmp_article_sort)
        except:
            tmp_article_sorts = []

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(articles, 5, request=request)
        articles = p.page(page)

        return render(request, 'study.html', {
            'active': 'study',
            'tmp_article_sorts': tmp_article_sorts,
            'articles': articles,
            'about_me': about_me,
            'new_articles': new_articles
        })

    def get(self, request):

        try:
            sort = request.GET.get('sort', 0)
        except:
            sort = 0

        if sort == 0:
            return self.get_total_html(request)
        else:
            return self.get_sort_html(request, int(sort))


class ArticlesView(View):

    def get_pre_next(self, datas, add_time):
        pre_articles = datas.filter(add_time__gt=add_time)
        next_articles = datas.filter(add_time__lt=add_time)

        pre_articles = pre_articles.order_by('add_time')
        next_articles = next_articles.order_by('-add_time')

        pre_len = pre_articles.count()
        next_len = next_articles.count()
        pre_flag = True
        next_flag = True
        if pre_len == 0:
            pre_flag = False

        if next_len == 0:
            next_flag = False

        if not pre_flag and not next_flag:
            return 'None', 'None'
        elif not pre_flag:
            return 'None', next_articles[0]
        elif not next_flag:
            return pre_articles[0] , 'None'
        else:
            return pre_articles[0], next_articles[0]

    def get(self, request):
        util = Util()
        try:
            article_id = request.GET.get('id', 1)
        except:
            article_id = 1

        try:
            send_sort = request.GET.get('sort', 0)
        except:
            send_sort = 0

        articles = ArticlesRecord.objects.order_by('-add_time')
        new_articles = articles[:5]
        article = articles.get(id=int(article_id))
        comments = SendCommentRecord.objects.filter(from_article=article)
        comments = comments.order_by('-add_time')

        writing = WritingsRecord.objects.filter(type='from_others')

        try:
            writing = util.selectData(
                datas = writing,
                data_len = writing.count(),
                select_len = 1
            )[0]
        except:
            writing = None

        article_sorts = ArticleSortRecord.objects.all()
        feelings_sort = article_sorts.get(name='Feelings')
        article_sort = ArticleSortRecord.objects.get(name=article.sort)
        article_sorts = util.selectData(
            datas = article_sorts,
            data_len = article_sorts.count(),
            select_len = 4
        )

        tmp_article_sorts = []
        colors = ['btn article-class-btn-color-1',
                  'btn article-class-btn-color-2',
                  'btn article-class-btn-color-3',
                  'btn article-class-btn-color-4']

        for _sort in article_sorts:
            index = random.randint(0, 3)
            tmp_article_sort = {
                'article_sort': _sort,
                'color': colors[index]
            }
            tmp_article_sorts.append(tmp_article_sort)


        if send_sort == 0 and article_sort.name != 'Feelings':
            articles = articles.filter(~Q(sort=feelings_sort))
            pre_article, next_article = self.get_pre_next(articles, article.add_time)
        else:
            pre_article, next_article = self.get_pre_next(articles.filter(sort=article_sort), article.add_time)

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        ignore_page_operation = IgnorePageOperation(int(page), int(math.ceil(comments.count() / 3.0)))
        pre_ignore_page, next_ignore_page = ignore_page_operation.getIgnorePage()

        p = Paginator(comments, 3, request=request)

        comments = p.page(page)

        head_images = PhotoShowRecord.objects.filter(image_type='headImg')
        head_images = util.selectData(
            datas=head_images,
            data_len=head_images.count(),
            select_len=5
        )

        try:
            head_image = head_images[0]
        except:
            head_image = None

        return render(request, 'article.html', {
            'active': 'study',
            'article': article,
            'comments': comments,
            'pre_article': pre_article,
            'next_article': next_article,
            'writing': writing,
            'tmp_article_sorts': tmp_article_sorts,
            'new_articles': new_articles,
            'send_sort': send_sort,
            'article_sort': article_sort,
            'not_feelings': article_sort.name != 'Feelings',
            'head_images': head_images,
            'first_image': head_image,
            'pre_ignore_page': pre_ignore_page,
            'next_ignore_page': next_ignore_page
        })


    def post(self, request):
        pass


class FeelingsView(View):
    def get(self, request):
        util = Util()
        try:
            sort = ArticleSortRecord.objects.filter(name='Feelings')[0]
        except:
            sort = None

        articles = ArticlesRecord.objects.order_by('-add_time')
        new_articles = articles[:5]
        articles = articles.filter(sort=sort)
        scenery_images = PhotoShowRecord.objects.filter(image_type='scenery')

        try:
            scenery_images = util.selectData(
                datas = scenery_images,
                data_len = scenery_images.count(),
                select_len = 2
            )
        except:
            scenery_images = None

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(articles, 6, request=request)
        articles = p.page(page)

        return render(request, 'feelings.html', {
            'active': 'feelings',
            'articles': articles,
            'article_sort': sort,
            'scenery_images': scenery_images,
            'new_articles': new_articles
        })





