#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/17 4:51 下午
# @Author  : Du Jincan
# @Email   : jincan.du@gmail.com
# @File    : main.py.py
# @Software: PyCharm

from aliyun_rds import get_download_url
from download_file import download_file
from mail_to_admin import mail_to_admin

RDS_ID = ''
accesskeyid = ''
accesssecret = ''
region_id = ''

directory = ''


backup_url, backup_filename = get_download_url(accesskeyid, accesssecret, region_id, RDS_ID)
output = download_file(backup_url, backup_filename, directory)

mail_context = "backup_file " + output
mail_conf = {'my_sender': ' ',
             'my_pass': ' ',
             'recipients': [" ", " "],
             'mail_context': mail_context,
             'mail_subject': ' ',
             'mail_server': " ",
             'port': 465,
             }

mail_to_admin(mail_conf)