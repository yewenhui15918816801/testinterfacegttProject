import unittest

from test_readconfig import ReadConfig, session

config = ReadConfig().httpconfig()
ReadConfig().test_login(config['url'])


class getProduct(unittest.TestCase):
    """获取已开发列表的接口测试用例"""
    def test_product(self):
        url = config['url'] + '/api/develope_product/getProducts'
        data = {"title": "", "pageIndex": 1, "pageSize": 50}
        res = session.post(url, json=data)
        self.assertIn("success", res.text)
        print("获取已开发的接口信息：", res.text)


if __name__ == '__main__':
    getProduct().test_product()
