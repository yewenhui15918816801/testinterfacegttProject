import json
import unittest
from common.logger import get_log
from test_readconfig import ReadConfig, session

config = ReadConfig().httpconfig()
ReadConfig().test_login(config['url'])
logger = get_log('product')


class getProduct(unittest.TestCase):
    def test_product(self):
        """获取已开发列表的接口测试用例"""
        url = config['url'] + '/api/develope_product/getProducts'
        data = {"title": "", "pageIndex": 1, "pageSize": 50}
        res = session.post(url, json=data)
        jsondata = json.loads(res.text)
        logger.info("获取已开发的接口信息的执行结果是:%s" % jsondata['status'])
        self.assertEqual("success", jsondata['status'])


if __name__ == '__main__':
    pass
