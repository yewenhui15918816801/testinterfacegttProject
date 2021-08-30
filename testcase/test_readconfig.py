import os
import configparser
import requests
from common.configuserDb import userDb

session = requests.session()


class ReadConfig:
    def httpconfig(self):
        httpDict = {}
        path = os.path.dirname(os.path.abspath(__file__))
        config_path = os.path.join(path, "../config.ini")
        config = configparser.ConfigParser()
        config.read(config_path)
        url = config.get('HTTP', 'url')
        timeout = config.get('HTTP', 'timeout')
        httpDict['url'] = url
        httpDict['timeout'] = timeout
        return httpDict

    def test_login(self, url):
        url_path = '/api/account/loginByToken'
        urlpath = url + url_path
        token = userDb().getToken()
        params = {"token": token['token']}
        res = session.post(urlpath, data=params)
        return res
