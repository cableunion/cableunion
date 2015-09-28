# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    '''
        关于user表的参考http://www.weiguda.com/blog/28/
    '''
    province = models.IntegerField(u'省', null=True, blank=True)
    city = models.IntegerField(u'市', null=True, blank=True)
    town = models.IntegerField(u'区', null=True, blank=True)
    nickname = models.CharField(u'昵称', max_length=50, null=True, blank=True)
    company_name = models.CharField(u'公司', max_length=100, null=True, blank=True)
    mobile = models.CharField(u'手机号', max_length=50, null=False, blank=False)
    postalcode = models.CharField(u'邮编', max_length=50, null=True, blank=True)
    industry = models.CharField(u'行业', max_length=50, null=True, blank=True)
    user_uuid = models.CharField(u'完成注册', max_length=50, null=False, blank=False)