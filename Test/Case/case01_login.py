import unittest
from Base.get_driver import GetDriver
from Page.page_login import PageLogin
from Test.Business.business_login import LoginBusiness
from Tools.get_log import GetLogger

log = GetLogger().get_logger()


class GSSLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 获取driver
        cls.driver = GetDriver().get_driver()
        # 初始化页面对象
        cls.login = LoginBusiness(cls.driver)

    @classmethod
    def tearDownClass(cls):
        GetDriver().quit_driver()

    def test_1(self):
        try:
            info_list = self.login.pwd_login(18113748898, 12345678)
            url = "https://gssdev.haoshengy.com/pc_workbench/workbench/overview"
        except Exception as error:
            self.login.base_screenshot()
            raise Exception("出错啦！", error)
        else:
            self.assertEqual(info_list[0], url)
            self.assertEqual(info_list[1], "概况总览")
