# coding: utf-8
"""
@author: oldman
@file: test_erweima_shibie.py
@time: 2020-09-24
"""
from pyzbar.pyzbar import decode
import cv2 as cv
import urllib.request as request
import numpy as np



"""
pip install pyzbar
pip install opencv-python
pip install zbar
"""

"""
图片包含二维码检测
"""
def qrcode_recongnize(filename):
    """
    :param filepath: 图片路径
    :param filename: 图片名字
    :return: 1 图片包含二维码，0 图片不包含二维码
    """
    image_type = []
    try:

        response = request.urlopen('http://jnxg.oss-cn-beijing.aliyuncs.com/UserFolders79684/5ol8hv9kpleh7ul7bqijsbn2qq.jpg')
        img_array = np.array(bytearray(response.read()), dtype=np.uint8)
        image = cv.imdecode(img_array, -1)

        # 解码二维码
        result = decode(image)

        if len(result)>0:
            image_type.append('qrcode')

        else:
            image_type.append('unqrcode')
    except:
        image_type.append('unqrcode')
    return image_type


if __name__ == "__main__":
    res = qrcode_recongnize("1.jpg")
    print(res)