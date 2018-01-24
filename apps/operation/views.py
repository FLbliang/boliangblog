# -*- coding: utf-8 -*-
# author: 'boliang'
# date: 2017/10/22 22:21


from django.shortcuts import render
from django.views.generic import View
from pure_pagination import Paginator, PageNotAnInteger
import math

from .models import SendMessageRecord, SendCommentRecord
from about_me.models import WritingsRecord
from articles_manage.models import ArticlesRecord
from photos_manage.models import PhotoShowRecord
from .forms import SendMessageForm, SendCommentForm
from utils.util import Util, HttpResponse, json, IgnorePageOperation

class MessageView(View):

    def get(self, request):
        print 'testsetestestsetestsstest'
        util = Util()

        send_messages = SendMessageRecord.objects.order_by('-add_time')
        writings = WritingsRecord.objects.filter(type='from_others')
        new_articles = ArticlesRecord.objects.order_by('-add_time')[:5]
        head_images = PhotoShowRecord.objects.filter(image_type='headImg')

        try:
            writings = util.selectData(
                    datas = writings,
                    data_len = writings.count(),
                    select_len = 1
            )[0]
        except:
            writings = None

        try:
            head_images = util.selectData(
                datas = head_images,
                data_len = head_images.count(),
                select_len = 5
            )
        except:
            head_images = None

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        ignore_page_operation = IgnorePageOperation(int(page), int(math.ceil(send_messages.count() / 4.0)))
        pre_ignore_page, next_ignore_page = ignore_page_operation.getIgnorePage()

        p = Paginator(send_messages, 4, request=request)
        send_messages = p.page(page)

        try:
            head_image = head_images[0]
        except:
            head_image = None

        return render(request, 'message.html', {
            'active': 'message',
            'send_messages': send_messages,
            'writings': writings,
            'new_articles': new_articles,
            'head_images': head_images,
            'top_headImage': head_image,
            'pre_ignore_page': pre_ignore_page,
            'next_ignore_page': next_ignore_page
        })

    def post(self, request):
        send_message_form = SendMessageForm(request.POST)

        util = Util()
        if send_message_form.is_valid():
            send_message_form.save(commit=True)
            message_records = SendMessageRecord.objects.order_by('-add_time')
            last_page = math.ceil(message_records.count() / 4.0)
            message_records = message_records[:4]
            return util.get_messages(request, message_records, last_page)
        else:
           return util.get_message_warnings(request)


class SendCommentView(View):
    def post(self, request):
        send_comment_form = SendCommentForm(request.POST)
        util = Util()
        if send_comment_form.is_valid():
            send_comment_form.save(commit=True)
            from_article_id = request.POST.get('from_article')
            article = ArticlesRecord.objects.get(id=from_article_id)
            message_records = SendCommentRecord.objects.filter(from_article=article)
            message_records = message_records.order_by('-add_time')
            last_page = int(math.ceil(message_records.count() / 3.0))
            message_records = message_records[:3]
            return util.get_messages(request, message_records, last_page)
        else:
           return util.get_message_warnings(request)


class SendGoodclicksView(View):
    def post(self, request):
        try:
            article_id = request.POST.get('article_id', 0)
        except:
            article_id = 0

        if article_id == 0:
            res = {
                'status': 'error'
            }
            return HttpResponse(json.dumps(res), content_type='application/json')

        article = ArticlesRecord.objects.get(id=int(article_id))
        article.good_clicks += 1
        article.save()
        res = {
            'status': 'success',
            'goodclick_nums': article.good_clicks
        }
        print 'test'
        return HttpResponse(json.dumps(res), content_type='application/json')

