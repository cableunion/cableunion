# -*- coding: utf-8 -*-
import datetime
from django.db import models
from ckeditor.fields import RichTextField


class Article(models.Model):
    TYPE_CHOICES = (
        (1, '电缆'), (2, '光缆'), (3, '原料'),
        (4, '橡胶'), (5, '招标'), (6, '企业'),
        (7, '会展'), (8, '国外'), (9, '龙头'),
        (10, '项目'),
    )
    title = models.CharField(u'标题', max_length=50, null=False, blank=False)
    type = models.SmallIntegerField(u'类型', choices=TYPE_CHOICES, null=False, blank=False) # [-32768 ,32767]的取值范围
    content = RichTextField(u'文章正文')
    create_time = models.DateTimeField(u'创建时间', null=False, blank=False, default=datetime.datetime.now())
    expires_time = models.DateTimeField(u'失效时间', null=False, blank=False, default=datetime.datetime.strptime('2500-01-01', '%Y-%m-%d'))

    class Meta:
        verbose_name = u'文章'
        verbose_name_plural = u'文章'
        db_table = 'article'
        app_label = 'article'
        ordering = ['create_time']
