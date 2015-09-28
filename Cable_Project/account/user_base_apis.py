# -*- coding: utf-8 -*-
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

