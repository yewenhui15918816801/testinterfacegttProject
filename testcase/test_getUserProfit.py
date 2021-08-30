import unittest

from test_readconfig import ReadConfig, session

config = ReadConfig().httpconfig()
ReadConfig().test_login(config['url'])


class getUserProfit(unittest.TestCase):
    """获取收益报表的接口测试用例"""
    def test_geruserprofit(self):
        url = config['url'] + '/api/develope_product/getUserProfit'
        data = {"user_id": "", "pageIndex": 1, "pageSize": 50, "user_ids": ["210610001"]}
        res = session.post(url, json=data)
        self.assertIn("success", res.text)
        print("获取收益报表的接口信息：", res.text)


if __name__ == '__main__':
    getUserProfit().test_geruserprofit()
