import unittest

from test_readconfig import ReadConfig, session

config = ReadConfig().httpconfig()
ReadConfig().test_login(config['url'])


class getOfficeProduct(unittest.TestCase):
    def test_getList(self):
        """获取新品开发列表的接口测试用例"""
        url = config['url'] + "/api/offline_develope/getOfflineProductsByCondition"
        data = {"pageIndex": 1, "pageSize": 50}
        res = session.post(url, json=data)
        self.assertIn("success", res.text)
        print("获取新品开发列表的接口：", res.text)


if __name__ == '__main__':
    pass
