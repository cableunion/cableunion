from django.shortcuts import render, render_to_response
from django.template import RequestContext
# Create your views here.


def welcome(request, template_name):
    vm = {}
    return render_to_response(template_name, vm, RequestContext(request))