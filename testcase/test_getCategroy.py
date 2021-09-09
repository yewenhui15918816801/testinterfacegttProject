import json
import unittest

from common.logger import get_log
from test_readconfig import ReadConfig, session

config = ReadConfig().httpconfig()
ReadConfig().test_login(config['url'])
logger = get_log('getCategory')


class getCategorylist(unittest.TestCase):
    """
       执行获取选品分类信息的接口的用例
    """
    def test_getList(self):
        url = 'http://172.168.20.13:9001/api/category/getCategoryList'
        res = session.post(url)
        self.assertIn("success", res.text)
        jsondata = json.loads(res.text)
        logger.info("获取选品分类信息的接口的执行结果是:%s"% jsondata['status'])


if __name__ == '__main__':
    pass
