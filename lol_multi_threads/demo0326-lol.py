# hxz
# 编写时间：2024/3/26  13:53
import os
import requests
import threading
import time


def download_skin(url, file_path):
    try:
        res = requests.get(url)
        if res.status_code == 200:
            with open(file_path, mode='wb') as f:
                f.write(res.content)
    except ConnectionError:
        pass


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
            url_skinPic = 'https://game.gtimg.cn/images/lol/act/img/skin/big' + skin['skinId'] + '.jpg'
            skin_name = skin['name']
            hero_name = skin['heroName']
            file_path = './pic/' + hero_name + '/' + skin_name.replace("/", "") + '.jpg'
            # 创建线程并启动
            t = threading.Thread(target=download_skin, args=(url_skinPic, file_path))
            t.start()


start = time.time()
func()
end = time.time()
print(end-start)


