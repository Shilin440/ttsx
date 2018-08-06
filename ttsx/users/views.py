from datetime import datetime, timedelta

from django.contrib.auth.hashers import check_password, make_password
from django.http import HttpResponseRedirect
from django.shortcuts import render

from django.urls import reverse

from users.models import UserModel, UserTicketModel
from utils.functions import get_ticket


def Login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        data = {}
        if not all([username, password]):
            data['msg'] = '请填写完整的用户名或密码'
        # 验证用户是否注册
        if UserModel.objects.filter(username=username).exists():
            user = UserModel.objects.get(username=username)
            # 验证密码是否正确
            if check_password(password, user.password):
                ticket = get_ticket()
                response = HttpResponseRedirect(reverse('ttsx:index'))
                out_time = datetime.now() + timedelta(days=1)
                response.set_cookie('ticket', ticket, expires=out_time)
                # 保存ticket值到数据库user_ticket表中
                UserTicketModel.objects.create(user=user,
                                               ticket=ticket,
                                               out_time=out_time)
                return response
            else:
                msg = '用户名或密码错误'
                return render(request, 'login.html', {'msg': msg})
        else:
            msg = '用户名不存在'
            return render(request, 'login.html', {'msg': msg})


def Register(request):
    if request.method == 'GET':
        return render(request, 'register.html')

    if request.method == 'POST':

        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_c = request.POST.get('password_c')
        # 如果提交的数据有为空的情况
        if not all([username, email, password, password_c]):
            data = {
                'msg': '请填写完整的信息'
            }
            return render(request, 'register.html', data)
        # 加密密码
        password = make_password(password)
        password_c = make_password(password_c)
        # 创建用户并添加到数据库
        UserModel.objects.create(username=username,
                                 password=password,
                                 password_c=password_c,
                                 email=email)

        return HttpResponseRedirect(reverse('user:login'))


def Logout(request):
    if request.method == 'GET':
        ticket = request.COOKIES.get('ticket')
        user_ticket = UserTicketModel.objects.filter(ticket=ticket).first()
        UserTicketModel.objects.filter(user=user_ticket.user).delete()
        return HttpResponseRedirect(reverse('user:login'))


# 用户中心跳转页面
def UserCenterInfo(request):
    if request.method == 'GET':
        return render(request, 'user_center_info.html')


def UserCenterOrder(request):
    if request.method == 'GET':
        return render(request, 'user_center_order.html')


def UserCenterSite(request):
    if request.method == 'GET':
        return render(request, 'usre_center_site.html')