import hashlib

import requests
# from pprint import  pprint

url='http://192.168.7.45:32013'

class libapis:

    def __init__(self):
        self.s=requests.Session()

    def output_md5(str_arg):
        """
        大写32位MD5加密
        :param str_arg:
        """
        str_md5 = '{}'.format(str_arg)
        str_md5 = str_md5.encode(encoding='utf-8')
        that_md5 = hashlib.md5(str_md5).hexdigest().upper()
        return that_md5

    def login(self,account,password,userid):
        response = self.s.post(url+'/api/UserLogin/AccountLogin',
                                 data={
                                     'account': account,
                                     'password': password,
                                     'userid':userid
                                 }
                                 )

        return response