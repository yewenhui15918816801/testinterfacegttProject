import unittest

from test_readconfig import ReadConfig, session

config = ReadConfig().httpconfig()
ReadConfig().test_login(config['url'])


class getStore(unittest.TestCase):
    """获取店铺追踪列表的接口测试用例"""
    def test_getData(self):
        url = config['url'] + '/api/watch_store/getProductsOfStore'
        data = {"sites": ["www.ebay.com", "www.ebay.ca", "www.ebay.de", "www.ebay.it", "www.ebay.co.uk", "www.ebay.es",
                          "www.ebay.fr", "www.ebay.at", "www.ebay.ch", "www.ebay.nl", "www.ebay.ie", "www.ebay.com.au"],
                "sort": "first_desc", "tagChange": "true", "notes": [], "noteIds": [], "pageIndex": 1, "pageSize": 50}
        res = session.post(url, json=data)
        self.assertIn("success", res.text)
        print("获取店铺追踪的接口信息：", res.text)


if __name__ == '__main__':
    getStore().test_getData()
