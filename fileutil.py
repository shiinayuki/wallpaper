# -*- coding: utf-8 -*-
"""
@Copyright (C) 2022 mewhaku . All Rights Reserved 
@Time ： 2022/7/7 12:06
@Author ： mewhaku
@File ：fileutil.py
@IDE ：PyCharm
"""
import os


# 保存HTML
def save_text(filename, data):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(data)


# 读取HTML
def read_text(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()


# 保存图片
def save_img(imgname, data):
    with open(imgname, 'wb') as f:
        f.write(data)


# 创建目录
def create_dir(path):
    # 判断这个目录是否存在
    isEX = os.path.exists(path)
    if not isEX:
        os.makedirs(path)

