# -*- coding: utf-8 -*-
import uuid
import json
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect, Http404
# shortcuts 捷径
from account.form import LoginForm, RegisterForm, revisePasswordForm
from account.user_base_apis import login_validate, set_email_url
from common.helper.send_email import set_email, send_email_main
from common.models.account import UserProfile


def account_common_view(request, template_name):
    vm = {

    }
    return render_to_response(template_name, vm, RequestContext(request))


@csrf_exempt
def _login(request):
    '''
        登录
    '''
    error = {'errMessage': ''}
    if request.method == 'POST':
        # print request.session.items()
        # print request.COOKIES
        if request.session.has_key('validate') and request.session['validate'].lower() == request.POST['captcha'].lower():
            form = LoginForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                username = data['username']
                password = data['password']
                if login_validate(request, username, password):
                    # print request.session.items()
                    # [(u'validate', u'4D3f'),
                    # ('_auth_user_hash', '12d158b95aa3a0a4500475bbe3cabc1ce167e157'),
                    # ('_auth_user_backend', 'django.contrib.auth.backends.ModelBackend'),
                    # ('_auth_user_id', 4L)]
                    # print request.COOKIES
                    # {'csrftoken': 'M47W6QDZjQd8cJTjAkGAY1iaTxnQ7Iyd', 'sessionid': 'mzbv8viq3mxr5w6tfgu6xiasyzcpaarf'}
                    return HttpResponseRedirect('/')
                else:
                    error['errMessage'] = '用户名或密码错误！'
            else:
                error['errMessage'] = form.errors
        else:
            error['errMessage'] = '验证码错误！'
    else:
        form = LoginForm()
    return render_to_response('login.html', error, RequestContext(request))


def _logout(request):
    '''
        退出
    '''
    # print request.session.items()
    # print request.COOKIES
    logout(request) # 没有返回值
    # print request.session.items()

    # print request.COOKIES
    # {'csrftoken': 'HrMsomwWlY9fg1etoKUXqCNJbdNKjP8H', 'sessionid': 'sbrvj8sc66o985vh7aj375s47lezlenj'}
    return HttpResponseRedirect('/')


@csrf_exempt
def register(request):
    '''
        注册
    '''
    error = {'errMessage': ''}
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            username = data['username']
            email = data['email']
            password = data['password']
            register_dict = {
                'company_name': data['company_name'],
                'province': data['province'],
                'city': data['city'],
                'town': data['town'],
                'mobile': data['mobile'],
                'postalcode': data['postalcode'],
                'industry': data['industry'],
                'is_active': False,
                'user_uuid': str(uuid.uuid1()).replace('-', '')
            }

            if not UserProfile.objects.filter(username=username) and not UserProfile.objects.filter(email=email):
                user = UserProfile.objects.create_user(username, email, password)
                user.company_name = register_dict['company_name']
                user.province = register_dict['province']
                user.city = register_dict['city']
                user.town = register_dict['town']
                user.mobile = register_dict['mobile']
                user.postalcode = register_dict['postalcode']
                user.industry = register_dict['industry']
                user.user_uuid = register_dict['user_uuid']
                user.is_active = False
                user.save()
                uu_url = set_email_url('register/', username, 'zllm')
                send_email_main(to_mail=email, user_uuid=uu_url, flag='login')
                return HttpResponseRedirect('/account/register/complete_prompt')
            elif UserProfile.objects.filter(username=username):
                error['errMessage'] = '用户名已存在！'
            elif UserProfile.objects.filter(email=email):
                error['errMessage'] = '该邮箱已经被注册！'
        else:
            error['errMessage'] = form.errors
    else:
        # django生成的表单
        form = RegisterForm()
    return render_to_response('register.html', error, RequestContext(request))


@csrf_exempt
def revise_password_check(request):
    '''
        重置密码，发送邮件和验证邮件
    '''
    template_name = 'register-complete-true-active.html'
    vm = {'content': ''}
    email = request.POST.get('email')
    if not UserProfile.objects.filter(email=email).exists():
        vm['errMessage'] = '该邮箱未注册！'
    else:
        uu_url = set_email_url('revise-password/', '', 'zllm')
        send_email_main(to_mail=email, user_uuid=uu_url, flag='revise')
        vm['content'] = '修改密码邮件已发送，请至邮箱查看！'
    return render_to_response(template_name, vm, RequestContext(request))


@csrf_exempt
def revise_password(request):
    '''
        重置密码
    '''
    vm = {'content': ''}
    form = revisePasswordForm(request.POST)
    user_uuid = request.POST.get('user_uuid')
    if form.is_valid():
        data = form.cleaned_data
        user = UserProfile.objects.get(user_uuid_exact=user_uuid)
        user.set_password(data['password'])
        user.save()
    else:
        form = revisePasswordForm()
    vm['content'] = u'密码修改成功，请用新密码重新登录！'
    return render_to_response('register-complete-true-active.html', vm, RequestContext(request))


def register_complete(request, user_uuid, template_name):
    vm = {'content': ''}
    userprofile = UserProfile.objects.filter(user_uuid=user_uuid)
    if userprofile.exists() and userprofile[0].is_active != 1:
        userprofile.update(is_active=1)
        vm['content'] = u'注册成功！'
    elif userprofile.exists() and userprofile[0].is_active == 1:
        vm['content'] = u'您以完成注册！'
    else:
        vm['content'] = u'用户不存在'

    return render_to_response(template_name, vm, RequestContext(request))


def check_handle(request):
    json_result = {'status': -1, 'message': ''}
    try:
        username = request.GET.get('username')
        email = request.GET.get('email')
        flag = request.GET.get('flag')
        if flag == 'username':
            if not UserProfile.objects.filter(username=username).exists():
                json_result['status'] = 1
        elif flag == 'email':
            if not UserProfile.objects.filter(email=email).exists():
                json_result['status'] = 1
    except Exception, e:
        json_result['status'] = -1
    return HttpResponse(json.dumps(json_result), 'application/json')