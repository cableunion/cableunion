__author__ = 'MXW'
from common.models.article import Article
from django.db.models import QuerySet


def home_article():
    iif_list = [1, 2, 3, 4, 5, 6] # Industry information
    pct_list = [7, 8, 9, 10] # Press control
    iif_query = Article.objects.filter(type__in=iif_list).query
    pct_query = Article.objects.filter(type__in=pct_list).query
    iif_query.group_by = ['type']
    pct_query.group_by = ['type']
    iif = QuerySet(query=iif_query, model=Article)
    pct = QuerySet(query=pct_query, model=Article)
    return iif, pct