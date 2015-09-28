# -*- coding: utf-8 -*-
from django.conf import settings
from django.contrib.auth.models import User, check_password

# django接入cas验证系统
class SettingsBackend(object):
    def authenticate(self, username=None, password=None):
        login_valid = (settings.ADMIN_LOGIN == username)
        pwd_valid = check_password(password, settings.ADMIN_PASSWORD)

        if login_valid and pwd_valid:
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                user = User(username=username, password='')
                user.is_staff = True
                user.is_superuser = True
                user.save()
                return user
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
