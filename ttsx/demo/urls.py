from django.conf.urls import url

from demo import views
#
urlpatterns = [
    # 首页
    url(r'^index/', views.Index, name='index'),
    # 商品列表
    url(r'^list/', views.List, name='list'),
    # 立即购买
    url(r'^cart/', views.Cart, name='cart'),
    # 减少商品
    url(r'^subgoods/', views.SubGoods, name='subgoods'),
    # 添加商品
    url(r'^addgoods/', views.AddGoods, name='addgoods'),
    # 详情页面
    url(r'^detail/', views.Detail, name='detail'),
    # 刷新增添与减少商品数量
    url(r'^goodsnum/', views.GoodsNum, name='goodsnum'),
    # 计算商品总价
    url(r'^tatalprice/', views.TatalPrice, name='tatalprice'),
    # 加入购物车
    url(r'^addcart/', views.AddCart, name='addcart'),
]