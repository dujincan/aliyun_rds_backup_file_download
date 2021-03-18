#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/17 2:36 下午
# @Author  : Du Jincan
# @Email   : jincan.du@gmail.com
# @File    : download_file.py
# @Software: PyCharm

import time
import requests
import os


def download_file(url, filename, directory):
    start = time.time()
    filepath = directory + filename
    response = requests.get(url, stream=True)

    size = 0
    chunk_size = 1024
    content_size = int(response.headers['content-length'])
    print("File size: " + str(content_size))

    try:
        print(f'Start download,[File size]:{content_size / 1024 / 1024:.2f} MB')
        with open(filepath, 'wb') as f:
            for data in response.iter_content(chunk_size=chunk_size):
                if data:
                    f.write(data)
                    size += len(data)
                    print('\r' + '[Downloading]:%s%.2f%%' % ('>' * int(size * 50 / content_size),
                                                             float(size / content_size * 100)), end=' ')
        end = time.time()
        print('Download completed!,times: %.2f秒' % (end - start))

    except:
        return_msg = "download failure"
        return return_msg

    if os.path.exists(filepath):
        fsize = os.path.getsize(filepath)
        print("Download file size: " + str(fsize))
        return_msg = "download successful!"
        if fsize == content_size:
            return return_msg

        else:
            return_msg = "download failure!"
            return return_msg
    else:
        return_msg = "download failure!"
        return return_msg
