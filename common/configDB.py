import logging

import pymysql


class Db():
    # 封装初始化的方法
    def __init__(self):
        self.mydb = pymysql.connect(host='172.168.20.13', port=3306, user='sa', password='Sellerpro',
                                    database='selection_pre_prod')
        self.cursor = self.mydb.cursor(cursor=pymysql.cursors.DictCursor)

    # 更新数据的方法
    def update(self, sql):
        try:
            self.cursor.execute(sql)
            self.mydb.commit()
        except Exception as e:
            self.mydb.rollback()
            print("在更新数据的时候，更新失败了{0}".format(e))

    # 关闭数据库连接
    def __del__(self):
        self.cursor.close()
        self.mydb.close()

    def insert(self, sql):
        try:
            self.cursor.execute(sql)
            self.mydb.commit()
        except Exception as e:
            self.mydb.rollback()
            print("在插入数据的时候插入失败了：{0}".format(e))

    # 封装查询的方法
    def select(self, sql, one):
        self.cursor.execute(sql)
        if one:
            data = self.cursor.fetchone()
        else:
            data = self.cursor.fetchall()
        return data

    # 封装删除的方法
    def _del(self, sql):
        self.cursor.execute(sql)

    # 获取上传文件的文件id
    def getFileID(self, sql):
        self.cursor.execute(sql)
        data = self.cursor.fetchone()
        return data

    # 获取上传文件的产品id
    def getProductID(self, sql):
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        return data
