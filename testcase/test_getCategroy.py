import unittest

from test_readconfig import ReadConfig, session

config = ReadConfig().httpconfig()
ReadConfig().test_login(config['url'])


class getCategorylist(unittest.TestCase):
    """

    """

    def test_getList(self):
        url = 'http://172.168.20.13:9001/api/category/getCategoryList'
        res = session.post(url)
        self.assertIn("success", res.text)
        print("获取选品分类信息的接口：", res.text)


if __name__ == '__main__':
    getCategorylist().test_getCategoryList()
