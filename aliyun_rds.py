#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/17 10:45 上午
# @Author  : Du Jincan
# @Email   : jincan.du@gmail.com
# @File    : aliyun_rds.py
# @Software: PyCharm

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException, ServerException
from aliyunsdkrds.request.v20140815.DescribeBackupsRequest import DescribeBackupsRequest


def get_download_url(keyid, secret, region, rds_id):
    """
    获取RDS实例备份文件的下载地址和文件名
    keyid: access-key-id
    secret: access-key-secret
    region: region-id
    rds_id: DBInstanceId
    """
    try:
        client = AcsClient(keyid, secret, region)
        request = DescribeBackupsRequest()
        request.set_accept_format('json')
        request.set_DBInstanceId(rds_id)

        response = client.do_action_with_exception(request)
        dic_tems = eval(response)
        url = dic_tems.get('Items').get('Backup')[0].get('BackupDownloadURL')
        filename = rds_id + "_" + url.split('?')[0].split('/')[-1]
        return url, filename
    except ClientException as e:
        print(e)
    except ServerException as e:
        print(e)
