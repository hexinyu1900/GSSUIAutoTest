import unittest
from Base.get_driver import BaseCase
from Test.Business.business_login import LoginBusiness
from Tools.get_log import GetLogger
from Base.get_driver import GetDriver
from Test.Business.business_one_unlock import *

log = GetLogger().get_logger()


class GSSOneUnlock(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 获取driver
        cls.driver = BaseCase.case_forward()
        # 初始化页面对象
        cls.one_unlock = OneUnlockBusiness(cls.driver)
        # 初始化面向对象
        # cls.login = LoginBusiness(cls.driver)
        cls.actityset = OneUnlockBusiness0(cls.driver)
        cls.pageset = PageSetBusiness(cls.driver)
        cls.unlockreward = UnlockRewardBusiness(cls.driver)
        cls.payset = PaySetBusiness(cls.driver)
        cls.posterpv = PosterPreviewBusiness(cls.driver)

    @classmethod
    def tearDownClass(cls):
        BaseCase.quit_driver()

    def test_1(self):
        """进入一元解锁模板页"""
        info_list = self.one_unlock.go_into_one_unlock_module_center()
        url = "https://gssdev.haoshengy.com/pc_workbench/workbench/marketing/temp-center"
        self.assertEqual(info_list[0], url, "url地址不正确 —— 用例不通过！")
        self.assertIn("一元解锁", info_list[1])  # 无法获取信息

    def test_2(self):
        """进入创建一元解锁活动页"""
        info = self.one_unlock.go_into_create_activity_page()
        self.assertEqual(info, "创建活动", "标题信息不一致 —— 用例不通过！")

    def test_3(self):
        """不采集信息-购买后不加微信-一阶活动"""
        try:
            # self.login.pwd_login('13778520754', 'Chenping147')
            self.actityset.page_setbusiness("pagetitle", 'wcsharetitle', 'wcsharedcribe', 0, 'ifaddlabel')
            self.pageset.page_set_business('ptvbcontent', 'ptcnaddress', 'tmtitletext', 'gcharacter')
            self.unlockreward.unlock_reward_business('uwpdctname', 'uwpdctitduction', 1, 199, 5, '0.1', 2, 'uwrwdct',
                                                     False, 5, 'umrwdct1')
            self.payset.pay_set_business(False, 'wqrsvdescrip')
            list_dir = self.posterpv.poster_preview_business('ptcprmendset', 0)
        except Exception as error:
            self.actityset.base_screenshot()
            raise Exception("出错啦！", error)
        else:
            self.assertEqual(list_dir[0], '海报预览')
            self.assertEqual(list_dir[1], '新建成功')
            self.assertEqual(list_dir[2], 'pagetitle', '活动列表第一个活动名称与创建活动名称不一致--用例不通过')

    def test_4(self):
        """采集信息-购买后不加微信-一阶活动-新增课程"""
        # 前置条件
        self.one_unlock.go_into_one_unlock_module_center()
        self.one_unlock.go_into_create_activity_page()
        try:
            self.actityset.page_setbusiness("pagetitle", 'wcsharetitle', 'wcsharedcribe', 1, 'ifaddlabel')
            self.pageset.page_set_business('ptvbcontent', 'ptcnaddress', 'tmtitletext', 'gcharacter')
            self.unlockreward.unlock_reward_business('uwpdctname', 'uwpdctitduction', 1, 199, 5, '0.1', 2, 'uwrwdct',
                                                     False, 5, 'umrwdct1')
            self.payset.pay_set_business(False, 'wqrsvdescrip')
            list_dir = self.posterpv.poster_preview_business('ptcprmendset', 1)
        except Exception as error:
            self.actityset.base_screenshot()
            raise Exception("出错啦！", error)
        else:
            self.assertEqual(list_dir[0], '海报预览')
            self.assertEqual(list_dir[1], '新建成功')
            self.assertEqual(list_dir[2], 'pagetitle', '活动列表第一个活动名称与创建活动名称不一致--用例不通过')

    def test_5(self):
        """不采集信息-购买后加微信-一阶活动"""
        # 前置条件
        self.one_unlock.go_into_one_unlock_module_center()
        self.one_unlock.go_into_create_activity_page()
        try:
            self.actityset.page_setbusiness("pagetitle", 'wcsharetitle', 'wcsharedcribe', 0, 'ifaddlabel')
            self.pageset.page_set_business('ptvbcontent', 'ptcnaddress', 'tmtitletext', 'gcharacter')
            self.unlockreward.unlock_reward_business('uwpdctname', 'uwpdctitduction', 1, 199, 5, '0.1', 2, 'uwrwdct',
                                                     False, 5, 'umrwdct1')
            self.payset.pay_set_business(True, 'wqrsvdescrip')
            list_dir = self.posterpv.poster_preview_business('ptcprmendset', 0)
        except Exception as error:
            self.actityset.base_screenshot()
            raise Exception("出错啦！", error)
        else:
            self.assertEqual(list_dir[0], '海报预览')
            self.assertEqual(list_dir[1], '新建成功')
            self.assertEqual(list_dir[2], 'pagetitle', '活动列表第一个活动名称与创建活动名称不一致--用例不通过')

    def test_6(self):
        """采集信息-购买后加微信-一阶活动"""
        # 前置条件
        self.one_unlock.go_into_one_unlock_module_center()
        self.one_unlock.go_into_create_activity_page()
        try:
            self.actityset.page_setbusiness("pagetitle", 'wcsharetitle', 'wcsharedcribe', 1, 'ifaddlabel')
            self.pageset.page_set_business('ptvbcontent', 'ptcnaddress', 'tmtitletext', 'gcharacter')
            self.unlockreward.unlock_reward_business('uwpdctname', 'uwpdctitduction', 1, 199, 5, '0.1', 2, 'uwrwdct',
                                                     False, 5, 'umrwdct1')
            self.payset.pay_set_business(True, 'wqrsvdescrip')
            list_dir = self.posterpv.poster_preview_business('ptcprmendset', 1)
        except Exception as error:
            self.actityset.base_screenshot()
            raise Exception("出错啦！", error)
        else:
            self.assertEqual(list_dir[0], '海报预览')
            self.assertEqual(list_dir[1], '新建成功')
            self.assertEqual(list_dir[2], 'pagetitle', '活动列表第一个活动名称与创建活动名称不一致--用例不通过')

    def test_7(self):
        """编辑活动"""
        info_list = self.one_unlock.edit_activity('测试编辑活动')
        self.assertEqual(info_list[0], "编辑成功", "提示信息不一致 —— 用例不通过！")
        self.assertEqual(info_list[1], "测试编辑活动", "活动名称不一致 —— 用例不通过！")

    def test_8(self):
        """分享活动"""
        info_list = self.one_unlock.share_activity()
        self.assertEqual(info_list[0], "活动页面", "标题信息不一致 —— 用例不通过！")
        self.assertEqual(info_list[1], "复制成功", "提示信息不一致 —— 用例不通过！")

    def test_9(self):
        """删除活动"""
        info_list = self.one_unlock.delete_activity()
        self.assertEqual(info_list[1], "删除成功", "提示信息不一致 —— 用例不通过")
        self.assertNotEqual(info_list[0], info_list[2], "两次活动名称一致 —— 用例不通过")

    def test_10(self):
        """复制活动"""
        info_list = self.one_unlock.copy_activity('测试复制活动')
        self.assertEqual(info_list[0], "新建成功", "提示信息不一致 —— 用例不通过！")
        self.assertEqual(info_list[1], "测试复制活动", "活动名称不一致 —— 用例不通过！")

    def test_11(self):
        """查看活动数据"""
        self.one_unlock.go_into_one_unlock_activity_details()
        info_list = self.one_unlock.go_into_activity_data()
        self.assertEqual(info_list[0], "访问人数", "页面标题不一致 —— 用例不通过！")
        self.assertEqual(info_list[1].split('?')[-1], "tab_section_id=t1", "url不正确 —— 用例不通过！")

    def test_12(self):
        """查看用户详情"""
        table_header = [
            '头像', '微信昵称', '性别', '降序', '传递级数', '购买状态'
        ]
        info_list = self.one_unlock.go_into_user_details(len(table_header))
        for i in range(len(table_header)):
            self.assertEqual(info_list[i], table_header[i], "表头不一致 —— 用例不通过！")
        self.assertEqual(info_list[-1].split('?')[-1], "tab_section_id=t3", "url不正确 —— 用例不通过！")

    def test_13(self):
        """查看预算分析"""
        info_list = self.one_unlock.go_into_budget_analysis()
        self.assertEqual(info_list[0], '红包消耗走势图', "页面标题不一致 —— 用例不通过！")
        self.assertEqual(info_list[-1].split('?')[-1], "tab_section_id=t4", "url不正确 —— 用例不通过！")

    def test_14(self):
        """查看基本信息"""
        info_list = self.one_unlock.go_into_basic_info()
        self.assertEqual(info_list[0], '页面信息', "页面标题不一致 —— 用例不通过！")
        self.assertEqual(info_list[-1].split('?')[-1], "tab_section_id=t5", "url不正确 —— 用例不通过！")

    def test_15(self):
        """查看活动订单"""
        table_header = [
            '序号', '手机号', '微信昵称', '支付金额', '支付时间', '支付状态', '操作'
        ]
        info_list = self.one_unlock.go_into_activity_order(len(table_header))
        for i in range(len(table_header)):
            self.assertEqual(info_list[i], table_header[i], "表头不一致 —— 用例不通过！")
        self.assertEqual(info_list[-1].split('?')[-1], "tab_section_id=t9", "url不正确 —— 用例不通过！")

