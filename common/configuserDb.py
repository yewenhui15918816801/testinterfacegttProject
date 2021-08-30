import pymysql


class userDb():
    # 封装初始化的方法
    def __init__(self):
        self.mydb = pymysql.connect(host='172.168.20.12', port=3306, user='sa', password='sellerpro1301',
                                    database='user-center')
        self.cursor = self.mydb.cursor(cursor=pymysql.cursors.DictCursor)

    # 获取用户中心token
    def getToken(self):
        sql = 'SELECT token FROM user_api_login_token WHERE `user_id` = 21526'
        self.cursor.execute(sql)
        token = self.cursor.fetchone()
        return token




