
import lib
# import unittest
# import pytest
import unittest

from .//lib/libsApi import libapis
import libsApi

class Test_login(unittest.TestCase):
    name = '登录'

    # 初始化方法
    def setup(self):
        pass

    #清除方法
    def teardown(self):
        pass

    def test_login_sus(self):
        login=lib.libapis().login('3927682',"${output_md5('12345678w')}",1002343)
        # self.assertEqual(0,login.json()['ret'])
        assert 0==login.json()['ret']

if __name__=='__main__':
    # unittest.main()
    unittest.main()