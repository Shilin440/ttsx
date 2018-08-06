from datetime import datetime, timedelta

from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password, make_password
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
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
            data['msg'] = '输入错误'
        if UserModel.objects.filter(username=username):
            user = UserModel.objects.get(username=username)
            if check_password(password, user.password):
                ticket = get_ticket()
                res = HttpResponseRedirect(reverse('ttsx:index'))
                out_time = datetime.now() + timedelta(days=1)
                res.set_cookie('ticket', ticket, expires=out_time)
                UserTicketModel.objects.create(user=user,
                                               ticket=ticket,
                                               out_time=out_time)
                return res
            else:
                data['msg'] = '输入错误'
        else:
            data['msg'] = '输入错误'
        return render(request, 'login.html', data)


def Register(request):
    if request.method == 'GET':
        return render(request, 'register.html')

    if request.method == 'POST':

        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        # 如果提交的数据有为空的情况
        if not all([username, email, password]):
            data = {
                'msg': '请填写完整的字段信息'
            }
            return render(request, 'register.html', data)

        UserModel.objects.create(username=username,
                                 password=make_password(password),
                                 email=email)

        return HttpResponseRedirect(reverse('user:login'))


def UserCenterInfo(request):
    if request.method == 'GET':
        return render(request, 'user_center_info.html')


def UserCenterOrder(request):
    if request.method == 'GET':
        return render(request, 'user_center_order.html')