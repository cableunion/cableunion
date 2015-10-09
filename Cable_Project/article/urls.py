# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns('article.views',
   # get article
   url(r'^content/(?P<article_id>\d+)/$', 'article_content', {'template_name': 'article-detail.html'}),
)
