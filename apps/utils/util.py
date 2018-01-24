# -*- coding: utf-8 -*-
# author: 'boliang'
# date: 2017/10/23 13:13


import random
import json
from django.http import HttpResponse


class IgnorePageOperation(object):
    def __init__(self, current_page, page_len):
        self.current_page = current_page
        self.page_len = page_len
        self.pre_ignore_page = None
        self.next_ignore_page = None

    def operation(self):
        pre_num = self.current_page - 3
        next_num = self.current_page + 4

        if pre_num > 1 and self.current_page < self.page_len-1:
            self.pre_ignore_page = pre_num
        elif pre_num > 1 and self.page_len-6 > 0 and self.page_len-6 < self.current_page:
            self.pre_ignore_page = self.page_len - 6
        else:
            self.pre_ignore_page = None

        if next_num == 5 and next_num < self.page_len:
            self.next_ignore_page = next_num+1 if next_num+1 < self.page_len else None
        else:
            self.next_ignore_page = next_num if next_num < self.page_len else None

    def getIgnorePage(self):
        self.operation()
        return self.pre_ignore_page, self.next_ignore_page


class DateOperation(object):
    def setDatetime(self, date):
        try:
            date = date.split(' ')
            self.year = int(date[0])
            self.month = int(date[1])
            self.day = int(date[2])
            self.hour = int(date[3])
            self.minute = int(date[4])
        except:
            raise Exception('date error')

    def get_realTime(self):

        self.hour = self.hour + 8
        if self.hour + self.minute / 60.0 > 24:
            self.handleTime()

        self.hour = str(self.hour) if self.hour >= 10 else '0'+str(self.hour)
        self.minute = str(self.minute) if self.minute >= 10 else '0'+str(self.minute)
        self.month = str(self.month)
        self.day = str(self.day)

        return u'{0}年{1}月{2}日 {3}:{4}'.format(
            self.year,
            self.month,
            self.day,
            self.hour,
            self.minute)

    def handleTime(self):
        self.hour = self.hour % 24
        month_range = self.monthRange(self.year, self.month)

        if self.day + 1 > month_range:

            remain = (self.month + 1) / 12
            self.month = (self.month + 1) % 12
            self.month = self.month if self.month else 1
            self.year = self.year + remain
            self.day = 1
        else:
            self.day = self.day + 1

    def isLeapYear(self, year):
        return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

    def monthRange(self, year, month):
        months = [[0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
                  [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]]

        flag = 0 if self.isLeapYear(year) else 1
        return months[flag][month]


class Util(object):
    def selectData(self, datas, data_len, select_len):
        if data_len == 0:
            return None
        else:
            select_indexs = range(data_len)
            random.shuffle(select_indexs)
            select_indexs = select_indexs[:select_len]
            res_datas = []
            for index in select_indexs:
                res_datas.append(datas[index])
            return res_datas

    def get_messages(self, request, message_records, last_page):
        messages = []
        date_operation = DateOperation()
        for message in message_records:
            try:
                date = message.add_time.strftime('%Y %m %d %H %M')
                date_operation.setDatetime(date)
                date = date_operation.get_realTime()
            except:
                date = 'system error'

            res_message = {
                'image': message.image, 'username': message.username,
                'add_time': date,
                'message': message.message,
            }
            messages.append(res_message)

        res = {
            'status': 'success',
            'messages': messages,
            'last_page': last_page,
        }

        return HttpResponse(json.dumps(res), content_type='application/json')

    def get_message_warnings(self, request):
        res = {'status': 'error', 'warning': u'邮箱格式错误或没有填写完必填信息!'}
        return HttpResponse(json.dumps(res), content_type='application/json')
