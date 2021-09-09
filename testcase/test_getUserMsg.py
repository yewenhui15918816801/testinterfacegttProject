import json
import unittest
from common.logger import get_log
from test_readconfig import ReadConfig, session

config = ReadConfig().httpconfig()
ReadConfig().test_login(config['url'])
logger = get_log('getUserMsg')


class getUserMsg(unittest.TestCase):
    def test_getData(self):
        """获取消息列表的接口测试用例"""
        url = config['url'] + '/api/message/getUserMsg'
        data = {"pageIndex": 1, "pageSize": 50}
        res = session.post(url, json=data)
        self.assertIn("success", res.text)
        jsondata = json.loads(res.text)
        logger.info("获取消息列表的接口信息：%s" % jsondata['status'])


if __name__ == '__main__':
    pass
