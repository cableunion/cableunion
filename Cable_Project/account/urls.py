# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from common.utils.captchas import get_captcha

urlpatterns = patterns('account.views',
    url(r'^$', 'account_common_view', {'template_name': 'welcome.html'}),
)

urlpatterns += patterns('account.views',
    # 登录
    url(r'^login/$', 'account_common_view', {'template_name': 'login.html'}),
    # 注册
    url(r'^register/$', 'account_common_view', {'template_name': 'register.html'}),
    # 重置密码
    url(r'^revise-password/$', 'account_common_view', {'template_name': 'revise-password.html'}),
    url(r'^revise-password/(?P<user_uuid>.*)/$', 'revise_password_callback', {'template_name': 'revise-password-urlcallback.html'}),
    # 完成注册
    url(r'^register/complete_prompt/$', 'account_common_view', {'template_name': 'register-complete-false-active.html'}),
    url(r'^register/(?P<user_uuid>.*)/$', 'register_complete', {'template_name': 'register-complete-true-active.html'}),
    # 验证码
    url(r'^captcha\.gif/$', get_captcha,),
)

urlpatterns += patterns('account.user_base',
    url(r'^login_views/$', '_login'),
    url(r'^logout_views/$', '_logout'),
    url(r'^register_views/$', 'register'),
    url(r'^revise_password_check/$', 'revise_password_check'),
    url(r'^revise_password/$', 'revise_password'),
    url(r'^register-check-handle/$', 'check_handle'),
)
