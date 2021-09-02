# -*- coding: utf-8 -*-

import unittest
from test_readconfig import ReadConfig, session

config = ReadConfig().httpconfig()
ReadConfig().test_login(config['url'])


class getERP(unittest.TestCase):
    def test_getData(self):
        """获取erp分类信息的接口测试用例"""
        url = 'http://172.168.20.13:9001/api/develope_product/getCategoryList'
        res = session.post(url)

        print("获取erp分类信息的接口：", res.text)
        return res


if __name__ == '__main__':
    getERP().test_getData()
