# -*- coding: utf-8 -*-
import json
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from common.models.account import UserProfile


def account_common_view(request, template_name):
    vm = {

    }
    return render_to_response(template_name, vm, RequestContext(request))


def register_complete(request, user_uuid, template_name):
    vm = {'content': ''}
    userprofile = UserProfile.objects.filter(user_uuid=user_uuid)
    if userprofile.exists() and userprofile[0].is_active != 1:
        userprofile.update(is_active=1)
        vm['content'] = u'注册成功！'
    elif userprofile.exists() and userprofile[0].is_active == 1:
        vm['content'] = u'您以完成注册！'
    else:
        vm['content'] = u'用户不存在'

    return render_to_response(template_name, vm, RequestContext(request))


def welcome(request, template_name):
    vm = {}
    return render_to_response(template_name, vm, RequestContext(request))