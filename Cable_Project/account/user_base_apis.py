# -*- coding: utf-8 -*-
import uuid
from django.contrib.auth import authenticate, login as auth_login


def login_validate(request, username, password):
    rtvalue = False
    user = authenticate(username=username, password=password) # 匹配到会返回一个User对象
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            return True
        else:
            # 用来做匿名用户
            pass
    return rtvalue


def set_email_url(url, uid, zllm):
    user_uuid = str(uuid.uuid1()).replace('-', '')
    uu_url = url + user_uuid + '/?uid={0}&zllm={1}&actionCode={2}'.format(uid, zllm, str(uuid.uuid1()))
    return uu_url