#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json

from io import BytesIO
from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from utils.check_code import create_validate_code
from repository import models
from ..forms.account import LoginForm

def jsonp(request):
    func = request.GET.get('callback')
    content = '%s(100000)' %(func,)
    return HttpResponse(content)


def check_code(request):
    """
    验证码
    :param request:
    :return:
    """
    stream = BytesIO()
    img, code = create_validate_code()
    img.save(stream, 'PNG')
    request.session['CheckCode'] = code
    return HttpResponse(stream.getvalue())


def login(request):
    """
    登陆
    :param request:
    :return:
    """
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        result = {'status': False, 'message': None, 'data': None}
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user_info = models.UserInfo.objects. \
                filter(username=username, password=password). \
                values('nid', 'nickname',
                       'username', 'email',
                       'avatar',
                       'blog__nid',
                       'blog__site').first()

            if not user_info:
                # result['message'] = {'__all__': '用户名或密码错误'}
                result['message'] = '用户名或密码错误'
            else:
                result['status'] = True
                request.session['user_info'] = user_info
                if form.cleaned_data.get('rmb'):
                    request.session.set_expiry(60 * 60 * 24 * 7)
        else:
            print(form.errors)
            if 'check_code' in form.errors:
                result['message'] = '验证码错误或者过期'
            else:
                result['message'] = '用户名或密码错误'
        return HttpResponse(json.dumps(result))
from web.forms.logincheck import MyForm
def register(request):
     """
    注册
    :param request:
    :return:
    """
     if request.method=="GET":
        obj = MyForm()
        return render(request, 'register2.html',{'obj':obj})
     elif request.method=="POST":
        obj = MyForm(request.POST)
        r1 = obj.is_valid()  #判断信息是否能够正确传递
        if r1:
        #     code = request.POST.get('check_code')
        #     if code.upper() == request.session['CheckCode'].upper():
        #         print obj.cleaned_data  #正确信息
        # else:
        #     print obj.errors #错误信息
            print obj.cleaned_data
            obj.save()
        else:
            print obj.errors
        return render(request, 'register2.html', {"obj":obj})
        # return redirect('/register.html')


def logout(request):
    """
    注销
    :param request:
    :return:
    """
    request.session.clear()

    return redirect('/')
