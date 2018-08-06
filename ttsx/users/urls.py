from django.conf.urls import url

from users import views

urlpatterns = [
    url(r'^login/', views.Login, name='login'),
    url(r'^register/', views.Register, name='register'),
    # 用户中心
    url(r'^user_center_info/', views.UserCenterInfo, name='user_center_info'),
    # 我的订单
    url(r'^user_center_order/', views.UserCenterOrder, name='user_center_order')
]