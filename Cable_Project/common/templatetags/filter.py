__author__ = 'MXW'
from django import template
from common.helper.enums import *
from django.conf import settings

register = template.Library()


@register.filter
def article_type_value(type):
    try:
        return ARTICLE_TYPE_VALUE[int(type)]
    except:
        return type

