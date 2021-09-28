import os
from time import sleep

from Page.page_one_unlock import PageOneUnlock
from Tools.select_image import SelectImage
from Config import Env_config

list_dir = []


class OneUnlockBusiness0(PageOneUnlock):
    def page_setbusiness(self, pagetitle, wcsharetitle, wcsharedcribe, info_switch, ifaddlabel):
        # # 点击模板中心
        # self.click_module_center()
        # # 点击一元解锁
        # self.select_one_unlock()
        # sleep(3)
        # # 选择模板
        # self.select_module()
        # 页面标题输入
        sleep(3)
        self.input_page_title(pagetitle)
        # 选择开始时间
        self.select_satrt_date()
        # 选择结束时间
        self.select_end_date()
        # 选择照片
        self.share_link_image(SelectImage.select_image(Env_config.image_path))
        # 微信分享标题
        self.wechat_share_title(wcsharetitle)
        # 微信分享描述
        self.wechat_share_describe(wcsharedcribe)
        # 是否采集报名信息
        if info_switch == 1:
            # 点击报名信息设置
            self.select_info_setting()
            for i in range(0, 5):
                # 点击取消标签
                self.If_cancel_course()
            for i in range(0, 5):
                # 点击增加课程
                self.If_add_labeling(ifaddlabel)
        else:
            self.nocollection_info()


class PageSetBusiness(PageOneUnlock):
    def page_set_business(self, ptvbcontent, ptcnaddress, tmtitletext, gcharacter):
        # 点击活动页面设置
        self.select_pageacty_setting()
        # 点击纯文本
        self.select_palin_text()
        # 纯文本文字内容输入信息
        self.Pt_verbal_content(ptvbcontent)
        # 纯文本链接地址输入内容
        self.Pt_chain_address(ptcnaddress)
        # 点击标题
        self.select_title_module()
        # 标题的标题文字输入信息
        self.Tm_title_text(tmtitletext)
        # # 点击图文内容
        # self.select_graphic_content()
        #
        # # 图文内容中的图片
        # time.sleep(3)
        # self.Gc_select_image(SelectImage.select_image(Env_config.image_path))
        # # 图文内容的添加图片按钮
        # self.Gc_add_image()
        # # 图文内容的添加文字按钮
        # self.Gc_add_character()
        # self.Gc_delete_button()
        # # 图文内容的添加文字的文案
        # self.Gc_copy_content(gcharacter)


class UnlockRewardBusiness(PageOneUnlock):
    def unlock_reward_business(self, uwpdctname, uwpdctitduction, uwactprice, uworgprice, uwquantity, uwdtbution,
                               uwrcmdfrd, uwrwdct, second_reward, uwrcmdfrd1, umrwdct1):
        # 点击解锁奖励设置
        self.select_share_warding()
        # 解锁奖励设置-商品名称输入信息
        self.Uw_product_name(uwpdctname)
        # 解锁奖励设置-商品介绍输入信息
        self.Uw_product_itduction(uwpdctitduction)
        # 解锁奖励设置-实际价格
        self.Uw_actual_price(uwactprice)
        # 解锁奖励设置-原价
        self.Uw_original_price(uworgprice)
        # 解锁奖励设置-库存数
        self.Uw_quantity(uwquantity)
        # 解锁奖励设置-分销奖励
        self.Uw_dstribution_rewards(uwdtbution)
        # 解锁奖励设置-第一阶段奖励的推荐好友报名
        self.Uw_recommend_friends(uwrcmdfrd)
        # 解锁奖励设置-第一阶段的奖励内容
        self.Uw_reward_content(uwrwdct)
        # 解锁奖励设置-第二阶奖励
        if second_reward == 1:
            self.base_scroll_bar()
            # 点击新增奖励
            self.Um_add_reward()
            self.base_scroll_bar()
            # 第二阶推荐好友报名
            self.Um_recommend_friends1(uwrcmdfrd1)
            # 第二阶奖励内容
            self.Um_reward_content1(umrwdct1)
        else:
            pass


class PaySetBusiness(PageOneUnlock):
    def pay_set_business(self, pay_setting, wqrsvdescrip):
        # 点击支付设置
        self.select_pay_setting()
        # 购买后是否加微信
        if pay_setting:
            # 点击支付设置的‘是’
            self.Wqr_switchyes()
            # 支付设置-上传二维码
            self.Wqr_wechat_scan(SelectImage.select_image(Env_config.image_path))
        else:
            pass
        # 服务说明
        self.Wqr_service_description(wqrsvdescrip)


class PosterPreviewBusiness(PageOneUnlock):
    def poster_preview_business(self, ptcprmendset, info_switch):
        # 点击海报设置
        self.select_poster_setting()
        # 海报设置-点击预览海报
        self.Pt_poster_preview()
        postpreviewtext = self.Pt_postpreview_text()
        list_dir.append(postpreviewtext)
        # 海报设置-关掉海报
        sleep(2)
        self.Pt_posterpreview_cancel()
        # 海报设置-复制推荐语设置
        self.Pt_copyrmend_setting(ptcprmendset)
        if info_switch == 1:
            self.select_setuocomplete2()
            self.select_setuocomplete1()
        else:
            self.select_setuocomplete()
            self.select_setuocomplete1()
        self.select_confirm_button()
        list_dir.append(self.new_success())
        list_dir.append(self.first_activity_title())
        return list_dir


class OneUnlockBusiness(PageOneUnlock):
    # 进入一元解锁模板页
    def go_into_one_unlock_module_center(self):
        self.click_module_center()
        self.select_one_unlock()
        infolist = list()
        infolist.append(self.get_current_url())
        infolist.append(self.get_module_info())
        return infolist

    # 进入一元解锁创建活动页
    def go_into_create_activity_page(self):
        self.select_module()
        sleep(2)
        info = self.get_create_activity_title()
        return info

    # 编辑活动
    def edit_activity(self, content):
        self.go_into_my_activity()
        self.click_edit_button()
        sleep(2)
        self.write_page_title_content(content)
        self.success_create_activity()
        infolist = list()
        infolist.append(self.get_message_info())
        infolist.append(self.get_activity_name())
        return infolist

    # 分享活动
    def share_activity(self):
        self.go_into_my_activity()
        self.click_share_button()
        infolist = list()
        infolist.append(self.share_window_title_info())
        self.click_copy_link()
        sleep(2)
        infolist.append(self.get_message_info())
        return infolist

    # 删除活动
    def delete_activity(self):
        self.go_into_my_activity()
        infolist = list()
        infolist.append(self.get_activity_name())
        self.click_delete_button()
        sleep(2)
        self.assert_delete()
        infolist.append(self.get_message_info())
        sleep(2)
        infolist.append(self.get_activity_name())
        return infolist

    # 复制活动
    def copy_activity(self, content):
        self.go_into_my_activity()
        sleep(2)
        self.click_copy_activity_button()
        # 选择日期
        self.select_begin_input()
        sleep(2)
        self.click_begin_next_page()
        self.click_begin_date()
        self.assert_begin_date()
        self.select_end_input()
        sleep(2)
        self.click_end_next_page()
        self.click_end_date()
        self.assert_end_date()
        # 编辑标题
        self.write_page_title_content(content)
        self.success_create_activity()
        infolist = list()
        infolist.append(self.get_message_info())
        infolist.append(self.get_activity_name())
        return infolist

    # 进入一元解锁活动详情
    def go_into_one_unlock_activity_details(self):
        self.go_into_my_activity()
        sleep(2)
        self.click_view_details_button()

    # 切换tab页至活动数据
    def go_into_activity_data(self):
        self.click_activity_data()
        info_list = list()
        info_list.append(self.get_activity_data_title_info())
        info_list.append(self.get_current_url())
        return info_list

    # 切换tab页至用户详情
    def go_into_user_details(self, num):
        self.click_user_details()
        info_list = list()
        for i in range(num):
            info_list.append(self.get_user_table_title(i))
        info_list.append(self.get_current_url())
        return info_list

    # 切换tab页至预算分析
    def go_into_budget_analysis(self):
        self.click_budget_analysis()
        info_list = list()
        info_list.append(self.get_budget_analysis_title())
        info_list.append(self.get_current_url())
        return info_list

    # 切换tab页至基本信息
    def go_into_basic_info(self):
        self.click_basic_info()
        info_list = list()
        info_list.append(self.get_basic_info_title())
        info_list.append(self.get_current_url())
        return info_list

    # 切换tab页至活动订单
    def go_into_activity_order(self, num):
        self.click_activity_order()
        info_list = list()
        for i in range(num):
            info_list.append(self.get_order_table_title(i))
        info_list.append(self.get_current_url())
        return info_list
