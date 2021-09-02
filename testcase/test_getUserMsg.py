import unittest

from test_readconfig import ReadConfig, session

config = ReadConfig().httpconfig()
ReadConfig().test_login(config['url'])


class getUserMsg(unittest.TestCase):
    def test_getData(self):
        """获取消息列表的接口测试用例"""
        url = config['url'] + '/api/message/getUserMsg'
        data = {"pageIndex": 1, "pageSize": 50}
        res = session.post(url, json=data)
        self.assertIn("success", res.text)
        print("获取消息列表的接口信息：", res.text)


if __name__ == '__main__':
    pass
