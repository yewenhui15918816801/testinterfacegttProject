import unittest

import requests
import configparser
import os
from common.configuserDb import userDb
from test_readconfig import ReadConfig

session = requests.session()
config = ReadConfig().httpconfig()


class login(unittest.TestCase):
    """获取登录的接口测试用例"""
    def test_login(self):
        url_path = '/api/account/loginByToken'
        urlpath = config['url'] + url_path
        token = userDb().getToken()
        params = {"token": token['token']}
        res = session.post(urlpath, data=params)
        print("获取登录接口的信息:", res.text)
        # 加入断言的结果
        self.assertIn("true", res.text)


if __name__ == '__main__':
    login().test_login()
