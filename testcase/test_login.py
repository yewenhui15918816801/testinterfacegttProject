import unittest
import requests
import configparser
import os
from common.configuserDb import userDb
from test_readconfig import ReadConfig
from common.logger import get_log


session = requests.session()
config = ReadConfig().httpconfig()
logger = get_log('login')


class login(unittest.TestCase):
    def test_login(self):
        """获取登录的接口测试用例"""
        url_path = '/api/account/loginByToken'
        urlpath = config['url'] + url_path
        token = userDb().getToken()
        params = {"token": token['token']}
        res = session.post(urlpath, data=params)
        logger.info("登录接口的执行结果是%s" % res.text)
        # 加入断言的结果
        self.assertIn("true", res.text)


if __name__ == '__main__':
    pass
