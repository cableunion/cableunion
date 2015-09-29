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
from account.form import LoginForm, RegisterForm
from account.user_base_apis import login_validate
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
        if request.session['validate'].lower() == request.POST['captcha'].lower():
            form = LoginForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                username = data['username']
                password = data['password']
                if login_validate(request, username, password):
                    return HttpResponseRedirect('/')
                else:
                    error['errMessage'] = '用户名或密码错误！'
        else:
            error['errMessage'] = '验证码错误！'
    else:
        form = LoginForm()
    return render_to_response('login.html', error, RequestContext(request))


def _logout(request):
    '''
        退出
    '''
    logout(request) # 没有返回值
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
                send_email_main(to_mail=email, user_uuid=register_dict['user_uuid'] + '/?uid={0}&zllm={1}&actionCode={2}'.format(username, 'zllm', str(uuid.uuid1())))
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


@login_required(login_url='/account/login/')
def revise_password(request):
    '''
        修改密码
    '''
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = UserProfile.objects.get(username_exact=username)
    user.set_password(password)
    user.save()
    return render_to_response('', {}, RequestContext(request))


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