# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Cable_Project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    url(r'^account/', include('account.urls')), # url(r'^account/$', include('account.urls')), 不能有结束符$
    url(r'', include('home.urls')),
    url(r'^category/', include('category.urls')),
    url(r'^article/', include('article.urls')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
)
