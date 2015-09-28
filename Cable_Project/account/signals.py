# -*- coding: utf-8 -*-
__author__ = 'MXW'
from django.db.models.signals import post_save
from django.contrib.auth.models import User

# 利用信号方法，当用户创建User时候，填充CustomUser模型实例。
def create_user_detail(sender, instance, signal, *args, **kwargs):
    print sender, instance, signal, args, kwargs
    from common.models.account import UserProfile
    if kwargs['created']:
        p = UserProfile()
        p.__dict__.update(instance.__dict__)
        p.save()

post_save.connect(create_user_detail, sender=User)