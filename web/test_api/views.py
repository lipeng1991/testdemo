# coding: utf-8
"""
@author: oldman
@file: views.py
@time: 2021-01-09
"""
import requests

from web.test_api.models import JnGoods


def async_data():
    url = "http://api.map.baidu.com/geocoding/v3/?output=json&address={" \
          "}&ak=w2KoHM46liHBl08zK12NZb10Vp4aCEmS&callback=showLocation "

    infos = JnGoods.objects.all()

    res = requests.get(url)

    print(res.json())