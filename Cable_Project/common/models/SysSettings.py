# -*- coding: utf-8 -*-
import datetime
from django.db import models


class ZLLMSysSettings(models.Model):
    code = models.CharField(u'配置key', max_length=50, null=False, blank=False)
    sys_value = models.TextField(u'配置的值', null=False, blank=False)
    comments = models.CharField(u'批注', max_length=300, null=False, blank=False)
    create_time = models.DateTimeField(u'创建时间', null=False, blank=False, default=datetime.datetime.now())

    class Meta:
        verbose_name = u'系统配置'
        verbose_name_plural = u'系统配置'
        db_table = 'zllm_syssettings'
