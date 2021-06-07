from Test.CaseSuite.suite_datail import CaseSuiteOpt


class CaseSuite(object):
    def __init__(self, case_list: list):
        self.case_list = case_list
        self.suite_opt = CaseSuiteOpt()
        self.case_opt = {
            101: self.suite_opt.case_suite_101, 102: self.suite_opt.case_suite_102
        }

    # 组合测试用例集
    def case_suite(self):
        for case in self.case_list:
            test_case = self.case_opt.get(case)
            test_case()
        return self.suite_opt.callback()

