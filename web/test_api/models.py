# coding: utf-8
"""
@author: oldman
@file: models.py
@time: 2021-01-09
"""
from django.db import models


class JnGoods:
    class Meta:
        db_table = "jnGoods"

    # 货物名称
    fromAddress = models.CharField(verbose_name="货物名称", max_length=1024, default="")
    # 货物类型
    takeGoodsAddress = models.CharField(verbose_name="货物类型", max_length=1024, default="")
    # 库存预警值 吨
    fromlng = models.DecimalField(verbose_name="经度", max_digits=10, decimal_places=6)
    fromlat = models.DecimalField(verbose_name="经度", max_digits=10, decimal_places=6)
    takegoodslng = models.DecimalField(verbose_name="经度", max_digits=10, decimal_places=6)
    takegoodslat = models.DecimalField(verbose_name="经度", max_digits=10, decimal_places=6)