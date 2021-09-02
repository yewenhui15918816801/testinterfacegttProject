import unittest
from common.logger import get_log
from test_readconfig import ReadConfig, session

config = ReadConfig().httpconfig()
ReadConfig().test_login(config['url'])
logger = get_log('userProfit')

class getUserProfit(unittest.TestCase):
    def test_geruserprofit(self):
        """获取收益报表的接口测试用例"""
        url = config['url'] + '/api/develope_product/getUserProfit'
        data = {"user_id": "", "pageIndex": 1, "pageSize": 50, "user_ids": ["210610001"]}
        res = session.post(url, json=data)
        self.assertIn("success", res.text)
        logger.info("获取收益报表的执行结果是%s" % res.text)


if __name__ == '__main__':
    pass
