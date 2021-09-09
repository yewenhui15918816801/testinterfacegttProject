import json
import jsonpath

# 用with的方法打开demo.json文件，需注意需要设置utf-8的编码格式
with open('demo.json', encoding='utf-8') as f:
    # print(f.read())
    data = f.read()
    # 将字符串类型的json转为字典型
    dict = json.loads(data)
    res1 = jsonpath.jsonpath(dict, '$..product_id')
    print(res1)
    print(type(res1))
    print(len(res1))

gttdata = ["233550521967", "233611437191", '233815183917', '233626314679', '373118961097', '233816523466',
           '233974142548', '123376260902'
    , '233832482929', '233974088787', '233814969862', '303851785355', '384345783669', '363334765621',
           '313269217927', '373666628307', '164538435332', '174158544595']


