from django.conf.urls import patterns, include, url


urlpatterns = patterns('category.views',
   url(r'^detail/(?P<cable_type>.*)/$', 'category_detail',),
)

