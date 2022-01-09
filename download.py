#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests  # 该模块需要自行安装

def download(url):  # 检查 URL 是否存在
    try:
        req = requests.get(url)
    except requests.exceptions.MissingSchema:
        print('Invalid URL "{}"'.format(url))
        return
    if req.status_code == 403:  # 检查是否成功访问了该网站
        print('You do not have the authority to access this page.')
        return
    filename = url.split('/')[-1]
    with open(filename, 'w') as fobj:
        fobj.write(req.content.decode('utf-8'))
    print("Download over.")

if __name__ == '__main__':
    url = input('Enter a URL: ')
    download(url)
'''
只有在当前模块名为 __main__ 的时候 (即作为脚本执行的时候) 才会执行此 if 块内的语句
当此文件以模块的形式导入到其它文件中时, if 块内的语句并不会执行
'''
