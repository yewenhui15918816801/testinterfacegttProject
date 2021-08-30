import unittest

from common.configDB import Db
from test_readconfig import ReadConfig, session

config = ReadConfig().httpconfig()
ReadConfig().test_login(config['url'])


class officeproduct(unittest.TestCase):
    def test_a_uploadfile(self):
        """上传文件的接口测试用例"""
        fo = open('D:\\testinterfaceProject\\ywh0806.xlsx', 'rb')
        files = {'file': fo}
        url = config['url'] + '/api/offline_develope/importProductsFromExcel'
        res = session.post(url, files=files)
        fo.close()
        self.assertIn("success", res.text)
        print("上传文件的接口信息：", res.text)

    def test_b_setcategory(self):
        """设置分类的接口测试用例"""
        url = config['url'] + '/api/offline_develope/setProductsCategory'
        sql = 'select id from offline_product  where title="ywhtesttesttesttesttest"'
        productinfo = Db().getProductID(sql=sql)
        data = {
            "erp_category_id": "8",
            "erp_category_name": "水管",
            "ids": [
                productinfo[0]['id']
            ]
        }
        res = session.post(url, json=data)
        self.assertIn("success", res.text)
        print("设置分类的接口信息：", res.text)

    def test_c_getproductinfo(self):
        """根据id获取线下产品的接口测试用例"""
        url = config['url'] + '/api/offline_develope/getProductById'
        sql = 'select id from offline_product  where title="ywhtesttesttesttesttest"'
        productinfo = Db().getProductID(sql=sql)
        data = {"id": productinfo[0]['id']}
        res = session.post(url, data=data)
        self.assertIn("success", res.text)
        print("根据id获取产品信息的接口：", res.text)

    def test_d_getallproduction(self):
        """获取全部产品的接口测试用例"""
        url = config['url'] + '/api/offline_develope/getOfflineProductsByCondition'
        res = session.post(url)
        self.assertIn("success", res.text)
        print("获取全部产品信息的接口：", res.text)

    def test_e_updateproductinfo(self):
        """更新产品信息的接口测试用例"""
        url = config['url'] + '/api/offline_develope/updateProduct'
        sql = 'select id from offline_product  where title="ywhtesttesttesttesttest"'
        productinfo = Db().getProductID(sql=sql)
        data = {
            "id": productinfo[0]['id'],
            "image": "http://172.168.20.13:9001/spu/fc6655f9-5ff3-4094-bf67-054a4e544962.jpg",
            "images": [
                "http://172.168.20.13:9001/spu/23041699-e541-4c34-b27c-bc6395dedd3d.jpg",
                "http://172.168.20.13:9001/spu/ee9bec1b-ad94-48fa-af92-9bd5f945f85b.jpg"
            ],
            "erp_category_id": "",
            "erp_category_name": "",
            "item_specifics": [{"name": "size", "values": ["1", "2"]}, {"name": "color", "values": ["红", "蓝"]}],
            "supplier": {"phone": "15918816808", "contact_name": "王五", "purchase_way": "2726493811",
                         "supplier_name": "广州卖家宝科技有限公司"},
            "supplier_name": "广州卖家宝科技有限公司",
            "links": [
                "https://gdjyym1.1688.com",
                "https://gdjyym1.1688.com"
            ],
            "description": "这是一段bdptest的描述"
        }
        res = session.post(url, json=data)
        self.assertIn("success", res.text)
        print("修改产品信息的接口：", res.text)

    def test_f_deleteproductinfo(self):
        """删除产品信息的接口测试用例"""
        url = config['url'] + '/api/offline_develope/delProducts'
        sql = 'select id from offline_product  where title="ywhtesttesttesttesttest"'
        productinfo = Db().getProductID(sql=sql)
        data = {
            "ids": [productinfo[0]['id']]
        }
        res = session.post(url, json=data)
        self.assertIn("success", res.text)
        print("删除产品信息的接口：", res.text)


if __name__ == '__main__':
    officeproduct().test_a_uploadfile()
    officeproduct().test_b_setcategory()
    officeproduct().test_c_getproductinfo()
    officeproduct().test_d_getallproduction()
    officeproduct().test_e_updateproductinfo()
    officeproduct().test_f_deleteproductinfo()