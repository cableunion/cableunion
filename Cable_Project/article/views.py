# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from common.models.article import Article


def article_content(request, article_id, template_name):
    article = Article.objects.get(id=article_id)
    vm = {
        'article': article
    }
    return render_to_response(template_name, vm, RequestContext(request))