# -*- coding: utf-8 -*-
from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(label=u'用户名', max_length=25, widget=forms.TextInput)
    email = forms.EmailField()
    password = forms.CharField(max_length=25, widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=25, widget=forms.PasswordInput)

    province = forms.IntegerField(required=False)
    city = forms.IntegerField(required=False)
    town = forms.IntegerField(required=False)

    nickname = forms.CharField(max_length=50, required=False)
    company_name = forms.CharField(max_length=50, required=False)
    mobile = forms.CharField(max_length=11)
    postalcode = forms.CharField(max_length=10, required=False)
    industry = forms.CharField(max_length=50, required=False)

    def pwd_validate(self, password, password2):
        return password == password2


class LoginForm(forms.Form):
    username = forms.CharField(label=u'用户名', max_length=25, widget=forms.TextInput)
    password = forms.CharField(label=u'密码', max_length=25, widget=forms.PasswordInput)

