from datetime import datetime, timedelta

from django.contrib.auth.hashers import check_password, make_password
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse

from demo.models import CartModel
from users.models import UserTicketModel, UserModel
from utils.functions import get_ticket


def Index(request):
    if request.method == 'GET':
        username = request.user.username
        data = {
            'username': username
        }
        return render(request, 'index.html', data)


def Cart(request):
    if request.method == 'GET':
        username = request.user.username
        data = {
            'username': username
        }
        return render(request, 'cart.html', data)


def AddCart(request):
    if request.method == 'POST':
        user = request.user
        data = {}
        data['code'] = ''
        if user.id:
            goods_id = request.POST.get('goods_id')
            cart = CartModel.objects.filter(user=user, goods_id=goods_id).first()
            if cart:
                cart.c_num += 1
                cart.save()
                data['c_num'] = cart.c_num
                data['code'] = '200'
                return JsonResponse(data)



def Detail(request):
    if request.method == 'GET':
        return render(request, 'detail.html')
    if request.method == 'POST':
        pass


def PlaceOrder(request):
    if request.method == 'GET':
        return render(request, 'place_order.html')