# -*- coding: utf-8 -*-
from django.db import models


class Wire(models.Model):
    cable_type = models.CharField(u'产品类型', max_length=50, null=False, blank=False, primary_key=True, unique=True)
    name = models.CharField(u'品名', max_length=50, null=False, blank=False)
    type = models.CharField(u'型号', max_length=50, null=False, blank=False)
    parameter = models.CharField(u'规格', max_length=50, null=False, blank=False)
    voltage = models.CharField(u'电压', max_length=50, null=True, blank=True)
    conductor = models.CharField(u'导体', max_length=50, null=True, blank=True)
    ampere = models.CharField(u'电流', max_length=50, null=True, blank=True)
    quality = models.CharField(u'特性', max_length=50, null=True, blank=True)
    manufacutre = models.CharField(u'厂家', max_length=50, null=True, blank=True)
    brand = models.CharField(u'品牌', max_length=50, null=True, blank=True)
    location = models.CharField(u'所在地', max_length=50, null=True, blank=True)
    description = models.CharField(u'详情说明', max_length=50, null=True, blank=True)
    price = models.FloatField(u'单价', null=False, blank=False)
    picture = models.ImageField(u'图片', upload_to='', null=False, blank=False)
    thumb_picture = models.ImageField(u'缩略图', null=True, upload_to='', blank=True)
    create_time = models.DateTimeField(auto_now_add=True, null=False, blank=False)


class MechanicalEquipment(models.Model):
    cable_type = models.CharField(u'产品类型', max_length=50, null=False, blank=False, primary_key=True, unique=True)
    name = models.CharField(u'品名', max_length=50, null=False, blank=False)
    model = models.CharField(u'机型', max_length=50, null=False, blank=False)
    pay_off_bobbin = models.CharField(u'放线盘', max_length=50, null=True, blank=True)
    take_up_bobbin = models.CharField(u'收线盘', max_length=50, null=True, blank=True)
    wire_diameter = models.CharField(u'适用线径', max_length=50, null=False, blank=False)
    max_twist_diameter = models.CharField(u'最大绞合外径', max_length=50, null=True, blank=True)
    lay_length = models.CharField(u'绞距', max_length=50, null=True, blank=True)
    rotate_speed = models.CharField(u'回转速', max_length=50, null=True, blank=True)
    take_up_tension = models.CharField(u'收线张力', max_length=50, null=True, blank=True)
    method_of_traverse = models.CharField(u'排线方式', max_length=50, null=True, blank=True)
    traverse_pitch = models.CharField(u'排线节距', max_length=50, null=True, blank=True)
    twist_direction = models.CharField(u'绞线方向', max_length=50, null=True, blank=True)
    taping_method = models.CharField(u'包带方式', max_length=50, null=True, blank=True)
    Load_and_unload_bobbin = models.CharField(u'上下线盘', max_length=50, null=True, blank=True)
    machine_size = models.CharField(u'机器尺寸', max_length=50, null=True, blank=True)
    total_weight = models.CharField(u'总重量', max_length=50, null=True, blank=True)
    price = models.FloatField(u'单价', null=False, blank=False)
    picture = models.ImageField(u'图片', null=False, blank=False)
    thumb_picture = models.ImageField(u'缩略图', null=True, blank=True)
    create_time = models.DateTimeField(auto_now_add=True, null=False, blank=False)


class Rubber(models.Model):
    cable_type = models.CharField(u'产品类型', max_length=50, null=False, blank=False, primary_key=True, unique=True)
    name = models.CharField(u'品名', max_length=50, null=False, blank=False)
    chemical_name = models.CharField(u'化学命名', max_length=50, null=True, blank=True)
    function = models.CharField(u'功能', max_length=50, null=True, blank=True)
    formula = models.CharField(u'配方', max_length=50, null=True, blank=True)
    standard = models.CharField(u'卫生指标', max_length=50, null=True, blank=True)
    description = models.CharField(u'简介', max_length=50, null=True, blank=True)
    price = models.FloatField(u'单价', null=False, blank=False)
    picture = models.ImageField(u'图片', null=False, blank=False)
    thumb_picture = models.ImageField(u'缩略图', null=True, blank=True)
    create_time = models.DateTimeField(auto_now_add=True, null=False, blank=False)
