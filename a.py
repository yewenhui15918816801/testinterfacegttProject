"""
作者：ywh
日期：2021/8/30
"""
import json
import jsonpath

# 用with的方法打开demo.json文件，需注意需要设置utf-8的编码格式
with open('demo.json', encoding='utf-8') as f:
    # print(f.read())
    data = f.read()
    # 将字符串类型的json转为字典型
    dict = json.loads(data)
    # 使用jsonpath提取出数据
    res1 = jsonpath.jsonpath(dict, '$..goods_id')
    print(len(res1))
    print(res1)



