import json
import logging
import unittest
from common.configDB import Db
from test_readconfig import ReadConfig, session
from common.logger import get_log
import ast



config = ReadConfig().httpconfig()
ReadConfig().test_login(config['url'])

logger = get_log('rule')


class rule(unittest.TestCase):
    def test_a_saverule(self):
        """创建规则的接口测试用例"""
        url = config['url'] + '/api/search_rule/saveSearchRule'
        data = {
            "searchRule": {
                "guice": 1111,
                "test": 2222
            },
            "name": "测试规则test"
        }
        res = session.post(url, json=data)
        result = ast.literal_eval(res.text)
        logger.info("创建规则执行结果是%s" % result['status'])
        self.assertIn("success", result['status'])


    def test_b_getrule(self):
        """获取规则信息的接口测试用例"""
        url = config['url'] + '/api/search_rule/getSearchRules'
        res = session.post(url)
        result = ast.literal_eval(res.text)
        logger.info("获取规则的执行结果是%s" % result['status'])
        self.assertIn("success", res.text)


    def test_c_updaterule(self):
        """更新规则信息的接口测试用例"""
        testsql = 'select id from search_rule where name="测试规则test"'
        r = Db().select(testsql, one=1)
        data = {
            "searchRule": {
                "规则1": 1111,
                "规则2": 2222
            },
            "ruleId": r['id'],
            "name": "testywh"
        }
        url = config['url'] + '/api/search_rule/updateSearchRule'
        res = session.post(url, json=data)
        logger.info("更新规则的执行结果是%s" % res.text)
        self.assertIn("success", res.text)


    def test_d_deleterule(self):
        """删除规则信息的接口测试用例"""
        try:
            testsql = 'select id from search_rule where name="testywh"'
            r = Db().select(testsql, one=1)
            data = {"ruleId": r['id']}
            url = config['url'] + '/api/search_rule/deleteSearchRule'
            res = session.post(url, data=data)
            logger.info("删除规则的执行结果是%s" % res.text)
            self.assertIn("success", res.text)
        except Exception as e:
            logger.warning("删除规则的时候抛出了异常{}:".format(e))


if __name__ == "__main__":
    pass
