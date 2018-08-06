from django.conf.urls import url

from users import views

urlpatterns = [
    # 注册
    url(r'^register/', views.Register, name='register'),
    # 登陆
    url(r'^login/', views.Login, name='login'),
    # 退出
    url(r'^logout/', views.Logout, name='logout'),
    # 用户信息页
    url(r'^user_center_info/', views.UserCenterInfo, name='user_center_info'),
    # 用户订单页
    url(r'^user_center_order/', views.UserCenterOrder, name='user_center_order'),
    # 用户收货地址页
    url(r'^user_center_site/', views.UserCenterSite, name='user_center_site'),
]