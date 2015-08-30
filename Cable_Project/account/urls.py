from django.conf.urls import patterns, include, url


urlpatterns = patterns('account.views',
    url(r'^$', 'welcome', {'template_name': 'welcome.html'}),
)
