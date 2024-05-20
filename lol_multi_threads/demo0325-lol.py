import time

import requests
import os
import json
from threading import Thread

"""
获取英雄联盟所有英雄信息
url:'https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js?v=20'
url结果返回有key：hero  这个key描述的是所有英雄信息和对应皮肤的列表
在hero列表中的元素，heroId描述的是英雄id，name指的英雄名

获取英雄数据以及皮肤信息url:'https://game.gtimg.cn/images/lol/act/img/js/hero/' + hero_id + '.js'
根据hero_id获取皮肤列表skins，每个皮肤都有皮肤名name和skinId，英雄有多少个皮肤他就有多少个skin

获取英雄皮肤图：https://game.gtimg.cn/images/lol/act/img/skin/big1004.jpg
'big1004.jpg'的组成 'big'+{skinId} +'.jpg'
"""


def func():
    url_herolist = 'https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js?v=20'
    res = requests.get(url_herolist)
    for i in res.json()['hero']:
        if not os.path.exists('./pic' + '/' + i['name']):
            print('./pic' + '/' + i['name'])
            # 文件夹名要根据英雄名来定义，一个文件夹只存储一个英雄的皮肤
            os.mkdir('./pic' + '/' + i['name'])
        url_skinslist = 'https://game.gtimg.cn/images/lol/act/img/js/hero/' + i["heroId"] + '.js'
        res_skins = requests.get(url_skinslist)
        for skin in res_skins.json()['skins']:
            url_skinpic = 'https://game.gtimg.cn/images/lol/act/img/skin/big' + skin['skinId'] + '.jpg'
            skin_name = skin['name']
            hero_name = skin['heroName']
            try:
                res_skins = requests.get(url_skinpic)
                if res_skins.status_code == 200:  # 如果遇到404 跳过
                    res_pic = res_skins.content
                    with open('./pic/' + hero_name + '/'+skin_name.replace("/", "")+'.jpg', mode='wb') as f:
                        # 处理掉文件名带斜杆的
                        f.write(res_pic)
            except ConnectionError:
                pass


start = time.time()
func()
end = time.time()
print(end-start)

"""
注：
1、储存英雄图片的方式可以用with open('xx.jpg', 'wb') as f: f.write(res.content)  res是接口请求的结果
2、文件夹名要根据英雄名来定义，一个文件夹只存储一个英雄的皮肤
3、python新建文件夹的方式（检索）
4、部分图片如果加载失败，需要用异常捕捉的方式跳过
5、如果遇到404 跳过
"""

# 结果截图1（代码截图）：
#
# 结果截图2（本地生成的效果）：
#
# 结果截图3（基于多线程实现）：
