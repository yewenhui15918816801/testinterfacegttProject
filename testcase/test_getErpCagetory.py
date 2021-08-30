# -*- coding: utf-8 -*-
import json
import unittest
from test_readconfig import ReadConfig, session

config = ReadConfig().httpconfig()
ReadConfig().test_login(config['url'])


class getERP(unittest.TestCase):
    """获取erp分类信息的接口测试用例"""
    def test_getData(self):
        url = 'http://172.168.20.13:9001/api/develope_product/getCategoryList'
        res = session.post(url)

        print("获取erp分类信息的接口：", res.text)
        return res


if __name__ == '__main__':
    getERP().test_getData()
