from django.http import JsonResponse
from django.shortcuts import render

from demo.models import GoodsValue, ArticleCategory, CartInfo


def Index(request):
    if request.method == 'GET':
        fresh_fruit = GoodsValue.objects.filter(gtype_id=1, isDelete=0)[0:4]
        seafood_aquaculture = GoodsValue.objects.filter(gtype_id=2, isDelete=0)[0:4]
        red_meat = GoodsValue.objects.filter(gtype_id=3, isDelete=0)[0:4]
        poultry_egg = GoodsValue.objects.filter(gtype_id=4, isDelete=0)[0:4]
        green_goods = GoodsValue.objects.filter(gtype_id=5, isDelete=0)[0:4]
        quick_frozen = GoodsValue.objects.filter(gtype_id=6, isDelete=0)[0:4]

        data = {
            'fresh_fruit': fresh_fruit,
            'seafood_aquaculture': seafood_aquaculture,
            'red_meat': red_meat,
            'poultry_egg': poultry_egg,
            'green_goods': green_goods,
            'quick_frozen': quick_frozen,
        }
        return render(request, 'index.html', data)


def List(request):
    if request.method == 'GET':
        kinds = ArticleCategory.objects.all()
        goods = GoodsValue.objects.filter(isDelete=0)
        tj_goods = GoodsValue.objects.filter(isDelete=0)[5:8]
        data = {
            'kinds': kinds,
            'goods': goods,
            'tj_goods': tj_goods
        }
        return render(request, 'list.html', data)


def Cart(request):
    if request.method == 'GET':
        return render(request, 'cart.html')


def AddGoods(request):
    if request.method == 'POST':
        user = request.user
        data = {}
        if user.id:
            goods_id = request.POST.get('goods_id')
            cart = CartInfo.objects.filter(user=user, goods_id=goods_id).first()
            if cart:
                cart.count += 1
                cart.save()
                data['count'] = cart.count
                data['goods_price'] = cart.goods.g_proce * cart.count
            else:
                CartInfo.objects.create(user=user, goods_id=goods_id)
                data['count'] = 1
            data['code'] = '200'
            data['msg'] = '请求成功'
            return JsonResponse(data)
        data['code'] = '1000'
        data['msg'] = '请登录后使用'
        return JsonResponse(data)


def SubGoods(request):
    if request.method == 'POST':
        user = request.user
        data = {}
        if user.id:
            goods_id = request.POST.get('goods_id')
            cart = CartInfo.objects.filter(user=user, goods_id=goods_id).first()
            if cart:
                if cart.count == 1:
                    data['msg'] = '不买拉倒'
                else:
                    cart.count -= 1
                    cart.save()
                    data['count'] = cart.count
                    data['goods_price'] = cart.goods.g_proce * cart.count
                data['code'] = '200'
                data['msg'] = '请求成功'
                return JsonResponse(data)
            else:
                data['msg'] = '请添加商品'
                return JsonResponse(data)
        else:
            data['code'] = '1001'
            data['msg'] = '请登录后使用'
            return JsonResponse(data)


def Detail(request):
    if request.method == 'GET':
        kinds = ArticleCategory.objects.all()
        g_id = request.GET.get('g_id')
        goods = GoodsValue.objects.filter(id=g_id).first()

        data = {
            'kinds': kinds,
            'goods': goods
        }
        return render(request, 'detail.html', data)

def GoodsNum(request):
    if request.method == 'GET':
        user = request.user
        cart_list = []
        if user.id:
            carts = CartInfo.objects.filter(user=user)
            for cart in carts:
                data = {
                    'id': cart.id,
                    'goods_id': cart.goods.id,
                    'count': cart.count,
                    'user_id': cart.user.id,
                }
                cart_list.append(data)
            data = {
                'carts': cart_list,
                'code': '200',
                'msg': '请求成功'
            }
            return JsonResponse(data)
        else:
            data = {
                'carts': '',
                'code': '1002',
                'msg': '请登录后再使用'
            }
            return JsonResponse(data)


def TatalPrice(request):
    if request.method == 'GET':
        user = request.user
        # 获取购物车中的商品信息
        carts = CartInfo.objects.filter(user=user)
        tatal_price = 0
        for cart in carts:
            tatal_price += cart.goods.g_price * cart.count
        # 总价保留2位小数
        tatal_price = round(tatal_price, 2)
        data = {
            'tatal_price': tatal_price,
            'code': '200',
            'msg': '请求成功'
        }
        return JsonResponse(data)


def AddCart(request):
    pass