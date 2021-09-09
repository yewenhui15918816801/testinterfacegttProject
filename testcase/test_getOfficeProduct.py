import json
import unittest
from common.logger import get_log
from test_readconfig import ReadConfig, session

config = ReadConfig().httpconfig()
ReadConfig().test_login(config['url'])
logger = get_log('officeProduct')


class getOfficeProduct(unittest.TestCase):
    def test_getList(self):
        """获取新品开发列表的接口测试用例"""
        url = config['url'] + "/api/offline_develope/getOfflineProductsByCondition"
        data = {"pageIndex": 1, "pageSize": 50}
        res = session.post(url, json=data)
        self.assertIn("success", res.text)
        jsondata = json.loads(res.text)
        logger.info("获取新品开发列表的接口的执行结果是:%s" % jsondata['status'])


if __name__ == '__main__':
    pass
