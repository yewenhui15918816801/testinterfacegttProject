# -*- coding: utf-8 -*-
import json
import unittest
from test_readconfig import ReadConfig, session
from common.logger import get_log

config = ReadConfig().httpconfig()
ReadConfig().test_login(config['url'])
logger = get_log('Gttproductinfo')


class getGttproduct(unittest.TestCase):
    def test_getData(self):
        """获取选品首页的接口测试用例"""
        url = config['url'] + '/api/crawl_product/searchCProductByRule'
        data = {
            "sort": "first_desc",
            "recent": 7,
            "pageSize": 200,
            "pageIndex": 2
        }
        res = session.post(url, json=data)
        gttproductdata = json.loads(res.text)
        self.assertIn("success", res.text)
        logger.info("根据条件获取选品首页的接口的执行结果是%s" % gttproductdata['status'])


if __name__ == '__main__':
    pass
