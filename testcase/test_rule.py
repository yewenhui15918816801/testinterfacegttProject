import logging
import unittest
from common.configDB import Db
from test_readconfig import ReadConfig, session

config = ReadConfig().httpconfig()
ReadConfig().test_login(config['url'])


class rule(unittest.TestCase):
    """创建规则的接口测试用例"""
    def test_a_saverule(self):
        url = config['url'] + '/api/search_rule/saveSearchRule'
        data = {
            "searchRule": {
                "guice": 1111,
                "test": 2222
            },
            "name": "测试规则test"
        }
        res = session.post(url, json=data)
        self.assertIn("success", res.text)
        print("保存规则接口的信息:", res.text)

    def test_b_getrule(self):
        """获取规则信息的接口测试用例"""
        url = config['url'] + '/api/search_rule/getSearchRules'
        res = session.post(url)
        self.assertIn("success", res.text)
        print("获取规则的接口: ", res.text)

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
        self.assertIn("success", res.text)
        print("更新搜索规则的接口：", res.text)

    def test_d_deleterule(self):
        """删除规则信息的接口测试用例"""
        try:
            testsql = 'select id from search_rule where name="testywh"'
            r = Db().select(testsql, one=1)
            data = {"ruleId": r['id']}
            url = config['url'] + '/api/search_rule/deleteSearchRule'
            res = session.post(url, data=data)
            print("删除搜索规则的接口:", res.text)
            self.assertIn("操作成功", res.text)
        except Exception as e:
            print("删除规则的时候抛出了异常{}:".format(e))


if __name__ == "__main__":
    rule().test_saverule()
    rule().test_getrule()
    rule().test_updaterule()
    rule().test_deleterule()
