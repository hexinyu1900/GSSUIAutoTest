import unittest
from Test.Case.case01_login import GSSLogin


class CaseSuiteOpt(object):

    def __init__(self):
        self.suite = unittest.TestSuite()

    # 登录测试集
    def case_suite_101(self):
        self.suite.addTest(GSSLogin('test_1'))

    # 一元解锁用例集
    def case_suite_102(self):
        pass

    def callback(self):
        return self.suite



