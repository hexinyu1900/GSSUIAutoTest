import unittest
from Test.Case.case01_login import GSSLogin


class CaseSuite:

    def __init__(self):
        self.suite = unittest.TestSuite()

    # 登录
    def case_suite(self):
        self.suite.addTest(GSSLogin('test_1'))
        return self.suite


if __name__ == '__main__':
    suite = CaseSuite().case_suite()
    runner = unittest.TextTestRunner()
    runner.run(suite)


