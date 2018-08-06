from django.db import models
from django.db.models import Model



from django.db import models

from users.models import UserModel


# 商品类型
class TypeInfo(models.Model):
    typename = models.CharField(max_length=30)
    isDelete = models.BooleanField(default=False)

    class Meta:
        db_table = 'typeinfo'



class Goods(models.Model):
    goodsname = models.CharField(max_length=30, unique=True)
    goodsid = models.CharField(max_length=10, unique=True, null=False, default='')
    goodspic = models.CharField(max_length=255, null=True)
    goodsprice = models.CharField(max_length=10)
    isDelete = models.BooleanField(default=False)
    goodsunit = models.CharField(max_length=20, default='克')  # 单位
    goodsclick = models.CharField(max_length=10, default='')  # 点击
    gjianjie = models.CharField(max_length=200, default='')
    gkucun = models.CharField(max_length=10, default='')
    gcontent = models.CharField(max_length=200, default='')
    gtype = models.ForeignKey(TypeInfo)  # 外键

    class Meta:
        db_table = 'goods'


class CartModel(models.Model):
    user = models.ForeignKey(UserModel)  # 关联用户
    goods = models.ForeignKey(Goods)  # 关联商品
    c_num = models.IntegerField(default=1)  # 商品的个数
    is_select = models.BooleanField(default=True)  #  是否选择商品

    class Meta:
        db_table = 'ttsx_cart'





# 商品模型
# class GoodsInfo(models.Model):
#     gtitle = models.CharField(u'名字', max_length=20)
#     gpic = models.ImageField(u'图片', upload_to='df_goods')
#     gprice = models.DecimalField(u'价钱', max_digits=5, decimal_places=2)
#     isDelete = models.BooleanField(default=False)
#     gunit = models.CharField(u'单位', max_length=20, default='500g')
#     gclick = models.IntegerField(u'点击')
#     gjianjie = models.CharField(max_length=200)
#     gkucun = models.IntegerField(u'库存')
    # gcontent = HTMLField(u'描述')
    # 引用外键
    # gtype=models.ForeignKey(TypeInfo)
    # 商品对象名字返回
    # def __str__(self):
    #     return self.gtitle.encode('utf-8')
    # class Meta:
    #     verbose_name_plural='水果'
