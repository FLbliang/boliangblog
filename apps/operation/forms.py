# -*- coding: utf-8 -*-
# author: 'boliang'
# date: 2017/10/24 23:16


from django import forms
import re

from .models import SendMessageRecord, SendCommentRecord


class SendMessageForm(forms.ModelForm):
    class Meta:
        model = SendMessageRecord
        fields = ['username', 'image', 'message', 'email', 'address']

    def clean_email(self):
        email = self.cleaned_data.get('email', '')
        if len(email) > 7:
            if re.match('^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$', email):
                return email

        raise forms.ValidationError(u'邮箱格式有误!')

    def __init__(self, *args, **kwargs):
        super(SendMessageForm, self).__init__(*args, **kwargs)
        self.fields['address'].required = False


class SendCommentForm(forms.ModelForm):
    class Meta:
        model = SendCommentRecord
        fields = ['from_article', 'username', 'image', 'message', 'email', 'address']

    def clean_email(self):
        email = self.cleaned_data.get('email', '')
        if len(email) > 7:
            if re.match('^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$', email):
                return email

        raise forms.ValidationError(u'邮箱格式有误!')

    def __init__(self, *args, **kwargs):
        super(SendCommentForm, self).__init__(*args, **kwargs)
        self.fields['address'].required = False

