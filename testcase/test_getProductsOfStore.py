import json
import unittest

from test_readconfig import ReadConfig, session
from common.logger import get_log

config = ReadConfig().httpconfig()
ReadConfig().test_login(config['url'])
logger = get_log('getProductsOfStore')


class getStore(unittest.TestCase):
    def test_getData(self):
        """获取店铺追踪列表的接口测试用例"""
        url = config['url'] + '/api/watch_store/getProductsOfStore'
        data = {"sites": ["www.ebay.com", "www.ebay.ca", "www.ebay.de", "www.ebay.it", "www.ebay.co.uk", "www.ebay.es",
                          "www.ebay.fr", "www.ebay.at", "www.ebay.ch", "www.ebay.nl", "www.ebay.ie", "www.ebay.com.au"],
                "sort": "first_desc", "tagChange": "true", "notes": [], "noteIds": [], "pageIndex": 1, "pageSize": 50}
        res = session.post(url, json=data)
        jsondata = json.loads(res.text)
        logger.info("获取店铺追踪的接口信息的执行结果是:%s" % jsondata['status'])
        self.assertEqual("success", jsondata['status'])

if __name__ == '__main__':
    pass
