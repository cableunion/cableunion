from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.contrib.sessions.backends.db import SessionStore
# Create your views here.
from home.apis import home_article


def group_by(key, Model, queryset):
    pass


def index(request, template_name):
    iif, pct = home_article()

    vm = {
        'iif': iif,
        'pct': pct
    }
    return render_to_response(template_name, vm, RequestContext(request))