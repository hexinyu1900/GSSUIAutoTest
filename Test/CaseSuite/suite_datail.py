import unittest
from Test.Case.case01_Login import GSSLogin
from Test.Case.case02_OneUnlock import GSSOneUnlock


class CaseSuiteOpt(object):

    def __init__(self):
        self.suite = unittest.TestSuite()

    # 登录测试集
    def case_suite_101(self):
        self.suite.addTest(GSSLogin('test_1'))

    # 一元解锁用例集
    def case_suite_102(self):
        # self.suite.addTest(GSSOneUnlock('test_1'))
        # self.suite.addTest(GSSOneUnlock('test_2'))
        # self.suite.addTest(GSSOneUnlock('test_3'))
        # self.suite.addTest(GSSOneUnlock('test_4'))
        # self.suite.addTest(GSSOneUnlock('test_5'))
        # self.suite.addTest(GSSOneUnlock('test_6'))
        # self.suite.addTest(GSSOneUnlock('test_7'))
        # self.suite.addTest(GSSOneUnlock('test_8'))
        self.suite.addTest(GSSOneUnlock('test_9'))
        # self.suite.addTest(GSSOneUnlock('test_10'))
        # self.suite.addTest(GSSOneUnlock('test_11'))
        # self.suite.addTest(GSSOneUnlock('test_12'))
        # self.suite.addTest(GSSOneUnlock('test_13'))
        # self.suite.addTest(GSSOneUnlock('test_14'))
        # self.suite.addTest(GSSOneUnlock('test_15'))

    def callback(self):
        return self.suite



