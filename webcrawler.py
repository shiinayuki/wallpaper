# -*- coding: utf-8 -*-
"""
@Copyright (C) 2022 mewhaku . All Rights Reserved 
@Time ： 2022/7/12 11:15
@Author ： mewhaku
@File ：webcrawler.py
@IDE ：PyCharm
"""
import requests
from lxml import etree
import os

"""
壁纸种类
wallpaper_type：

电脑壁纸 = "dnbz"
手机壁纸 = "sjbz"
4K壁纸 = "4kbz"

细分种类
detail_type:

动漫原画 = "?q=--82--.html"
卡通动漫 = "?q=--81--.html"
航天飞机 = "?q=--80--.html"
自然风景 = "?q=--79--.html"
花卉植物 = "?q=--78--.html"
绘画创意 = "?q=--77--.html"
动物萌宠 = "?q=--76--.html"
家居陈设 = "?q=--75--.html"
静物特写 = "?q=--74--.html"
肌理纹理 = "?q=--89--.html"
军事科技 = "?q=--72--.html"
明星大咖 = "?q=--71--.html"
太空科幻 = "?q=--70--.html"
禅意古风 = "?q=--69--.html"
体育运动 = "?q=--85--.html"
美女写真 = "?q=--65--.html"
人文风土 = "?q=--87--.html"
美食甜品 = "?q=--88--.html"
城市建筑 = "?q=--83--.html"
汽车船舶 = "?q=--84--.html"
影视剧照 = "?q=--90--.html"
情感文艺 = "?q=--91--.html"

页面 
page = "i"

"""


class Scrape():
    # 初始化
    def __init__(self, wallpaper_type, detail_type, page):
        self.url = f"https://www.toopic.cn/{wallpaper_type}/{detail_type}&page={page}"

        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Safari/537.36 Edg/103.0.1264.44"
        }

    # 发送url，得到页面数据
    def get_data(self):
        response = requests.get(self.url, headers=self.headers)
        return response.text

    # 对页面数据进行解析,得到ul下面的img地址
    def parse_page(self, data, li_path, img_path):
        mytext = etree.HTML(data)
        mytext = mytext.xpath(li_path)
        mytext = mytext[0].xpath(img_path)
        return mytext

    def get_byte(self, img_data):
        response = requests.get("https://www.toopic.cn/" + img_data, headers=self.headers)
        return response.content

    # 解析列表页，得到主要内容
    def parse_index_page(self, data, li_path):
        mytext = etree.HTML(data)
        mytext = mytext.xpath(li_path)
        return etree.tostring(mytext[0])

    # 解析列表处理页，得到超链接的url
    def parse_index_url(self, data, page_xpath):
        mytext = etree.HTML(data)
        mytext = mytext.xpath(page_xpath)
        return mytext

    # 打开文件夹
    def open_file(self):
        start_directory = r'..\true'
        os.system("explorer.exe %s" % start_directory)

    # 删除空html
    def file_check(self,wt, dt, page):

        file = f"../true/{wt}{dt}未处理html/第{page}页.html"
        if os.path.exists(file):
            if os.path.getsize(file) <= 25000:
                os.remove(file)
                return True
            else:
                return False
        else:
            return False

