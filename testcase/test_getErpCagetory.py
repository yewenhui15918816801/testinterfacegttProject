# -*- coding: utf-8 -*-
import json
import unittest
from test_readconfig import ReadConfig, session
from common.logger import get_log

config = ReadConfig().httpconfig()
ReadConfig().test_login(config['url'])
logger = get_log('getErpCagetory')


class getERP(unittest.TestCase):
    def test_getData(self):
        """获取erp分类信息的接口测试用例"""
        url = 'http://172.168.20.13:9001/api/develope_product/getCategoryList'
        res = session.post(url)
        jsondata = json.loads(res.text)
        logger.info("获取erp分类数据接口的执行结果是:%s" % jsondata['status'])


if __name__ == '__main__':
    pass
