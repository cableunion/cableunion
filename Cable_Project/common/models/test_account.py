# -*- coding: utf-8 -*-
# 这里是建立用户表的参考 2中方式

from django.db import models
from django.contrib.auth.models import User, UserManager
from django.contrib.auth.admin import UserAdmin


class ProfileBase(type):
    def __new__(cls, name, bases, attrs): # 当前准备创建的类的对象, 类的名字, 类继承的父类集合, 类的方法集合
        module = attrs.pop('__module__')
        parents = [b for b in bases if isinstance(b, ProfileBase)]
        if parents:
            fields = []
            for obj_name, obj in attrs.items():
                if isinstance(obj, models.Field):
                    fields.append(obj_name)
                    User.add_to_class(obj_name, obj)
            UserAdmin.fieldsets = list(UserAdmin.fieldsets)
            UserAdmin.fieldsets.append((name, {'fields': fields}))
        return super(ProfileBase, cls).__new__(cls, name, bases, attrs)


class Profile(object):
    '''
        元类
        除了使用type()动态创建类以外，要控制类的创建行为，还可以使用metaclass
    '''
    __metaclass__ = ProfileBase


class MyProfile(Profile):
    province = models.IntegerField(u'省', null=True, blank=True)
    city = models.IntegerField(u'市', null=True, blank=True)
    town = models.IntegerField(u'区', null=True, blank=True)
    nickname = models.CharField(u'昵称', max_length=50, null=True, blank=True)
    company_name = models.CharField(u'公司', max_length=100, null=True, blank=True)
    mobile = models.CharField(u'手机号', models=50, null=False, blank=False)
    postalcode = models.CharField(u'邮编', models=50, null=True, blank=True)
    industry = models.CharField(u'行业', models=50, null=True, blank=True)


# coding: utf8
# Create your models here.
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


class AuthUser(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(max_length=40, unique=True, db_index=True)
    email = models.EmailField(max_length=254, unique=True)
    avatar = models.ImageField(upload_to='avatar')
    nickname = models.CharField(max_length=60)

    is_staff = models.BooleanField('staff status', default=False)
    is_active = models.BooleanField('active', default=True)

    bio = models.CharField(max_length=255)

    GENRE_CHOICES = (
        (1, '摄影师'),
        (2, '插画师'),
        (3, '原画师'),
        (4, '平面设计师'),
        (5, '品牌顾问'),
        (6, '其他'),
    )
    genre = models.SmallIntegerField(choices=GENRE_CHOICES)
    site_dribbble = models.URLField(blank=True, verbose_name=u'Dribbble')
    site_deviantart = models.URLField(blank=True, verbose_name=u'DeviantART')
    site_benhance = models.URLField(blank=True, verbose_name=u'Benhance')
    site_tumblr = models.URLField(blank=True, verbose_name=u'Tumblr')
    site_zcool = models.URLField(blank=True, verbose_name=u'站酷')
    site_blog = models.URLField(blank=True, verbose_name=u'博客')
    site_sina = models.URLField(blank=True, verbose_name=u'新浪微博')

    ''' 【提示就这里语法错误！！！】 '''
    ''' 用于登录的字段 '''
    USERNAME_FIELD = 'username'
    '''
        REQUIRED_FIELDS must contain all required fields on your User model,
        but should not contain the USERNAME_FIELD or password as these fields
        will always be prompted for.
    '''
    REQUIRED_FIELD = ['email']

    objects = UserManager()

    def get_full_name(self):
        return self.nickname

    def get_short_name(self):
        return self.nickname

    def __unicode__(self):
        return self.username


class UserManager(BaseUserManager):

    def create_user(self, username, email, password=None):

        ''' create_user()参数必须是USERNAME_FIELD 和 所有的REQUIRED_FIELD '''

        if not email:
            raise ValueError('用户必须输入Email地址')

        user = self.model(
            username=username,
            email=UserManager.normalize_email(email),
            is_staff=False,
            is_active=True,
            is_superuser=False
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):

        user = self.create_user(
            username=username,
            email=email,
            password=password
        )

        user.is_staff = True
        user.is_active = True
        user.is_superuser = True

        user.save(using=self._db)
        return user


# class Article(models.Model):
#         author = models.ForeignKey(settings.AUTH_USER_MODEL)
#         title = models.CharField(max_length=255)
