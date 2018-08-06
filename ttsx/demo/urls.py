from django.conf.urls import url


from demo import views

urlpatterns = [
    url(r'^index/', views.Index, name='index'),
    #购物车
    url(r'^cart/', views.Cart, name='cart'),
    # 添加购物车
    url(r'^addcart/', views.AddCart, name='addcart'),
    # 商品详情
    url(r'^detail/', views.Detail, name='detail'),
    # 支付页面
    url(r'^place_order/', views.PlaceOrder, name='place_order')
]