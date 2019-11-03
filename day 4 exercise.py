#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
案例：
有N个人要参加会议，现在需要随机安排座位。
请用python实现将N个人随机安排座位
"""
name = """
邓永明    廖德超    张勇 杨久林    戴贵富    秦代坤    李元东 田显余
"""

# 2. 办公室名字
import random
site_list = ['1号办公室1位置', '1号办公室2位置', '1号办公室3位置',
             '2号办公室1位置', '2号办公室2位置', '2号办公室3位置',
             '3号办公室1位置', '3号办公室2位置']
name = '邓永明    廖德超    张勇 杨久林    戴贵富    秦代坤    李元东 田显余'
name1=name.split()
stable = {}
for i in name1:
    v = random.choice(site_list)
    stable['%s'%i] = v
    site_list.remove(v)
print(stable)

"""
运行下面代码之后会的到一个非常复杂的字典，
要求：从字典中提取歌手、歌名、音乐地址
"""

import requests
import pprint

response = requests.get('http://musicapi.taihe.com/v1/restserver/ting?method=baidu.ting.song.playAAC&format=json&songid=100575177 ')
data = response.json()
pprint.pprint(data)

v1 = data['songinfo']['artist']
v2 = data['songinfo']['title']
v3 = data['songinfo']['lrclink']
print('"歌手:{}","歌名:{}","歌词:{}"'.format(v1,v2,v3))