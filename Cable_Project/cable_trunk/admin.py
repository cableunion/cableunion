# -*- coding: utf-8 -*-
from django.contrib import admin
from common.models.account import UserProfile
from common.models.article import Article
from common.models.category import Wire, MechanicalEquipment, Rubber
# Register your models here.

# eg:
# class AuthorAdmin(admin.ModelAdmin):
#     list_display=('name','age','sex')   #列表显示
#     search_fields=('name',)             #搜索
#     list_filter = ('type',)             #过滤器
#     date_hierarchy = 'birth'            #日期型字段进行层次划分。
#     ordering = ('-birth','age')         #对出生日期降序排列，对年级升序
#     fields = ('name','sex','age','birth','type')    #自定义编辑表单，在编辑表单的时候 显示哪些字段，显示的属性


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_active', 'date_joined', 'last_login', )
    ordering = ('-date_joined', )


class WireAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'parameter', 'create_time', )
    ordering = ('-create_time', )


class MechanicalEquipmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'create_time', )
    ordering = ('-create_time', )


class RubberAdmin(admin.ModelAdmin):
    list_display = ('name', 'chemical_name', 'create_time', )
    ordering = ('-create_time', )


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'create_time', )


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Wire, WireAdmin)
admin.site.register(MechanicalEquipment, MechanicalEquipmentAdmin)
admin.site.register(Rubber, RubberAdmin)
admin.site.register(Article, ArticleAdmin)