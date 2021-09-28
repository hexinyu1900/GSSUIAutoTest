from Base.base import Base
from Config import OneUnlock_config


class PageOneUnlock(Base):
    # 点击模板中心
    def click_module_center(self):
        self.base_click(OneUnlock_config.ModuleCenterClick)

    # 活动类型选择一元解锁
    def select_one_unlock(self):
        self.base_click(OneUnlock_config.OneUnlockClick)

    # 获取模板介绍信息
    def get_module_info(self):
        return self.base_get_text(OneUnlock_config.ModuleInfo)

    # 选择模板
    def select_module(self):
        self.base_click(OneUnlock_config.ModuleClick)

    # 选择取消
    def select_cancel(self):
        self.base_click(OneUnlock_config.CancelButton)

    # 选择设置完成,马上生成活动
    def select_setuocomplete(self):
        self.base_click(OneUnlock_config.SetupComplete)

    def select_setuocomplete1(self):
        self.base_click(OneUnlock_config.SetupComplete1)

    def select_setuocomplete2(self):
        self.base_click(OneUnlock_config.SetupComplete2)

    # 确认生成活动
    def select_confirm_button(self):
        self.base_click(OneUnlock_config.ConfirmButton)

    # 活动设置
    def select_activity_setting(self):
        self.base_click(OneUnlock_config.ActivitySetting)

    # 活动页面设置
    def select_pageacty_setting(self):
        self.base_click(OneUnlock_config.ActivityPageSetting)

    # 解锁奖励设置
    def select_share_warding(self):
        self.base_click(OneUnlock_config.UnlockWardingSetting)

    # 支付设置
    def select_pay_setting(self):
        self.base_click(OneUnlock_config.PaySetting)

    # 海报设置
    def select_poster_setting(self):
        self.base_click(OneUnlock_config.PosterSetting)

    # 报名信息设置
    def select_info_setting(self):
        self.base_click(OneUnlock_config.InfoSetting)

    # 填写页面标题
    def input_page_title(self, values):
        self.base_clear(OneUnlock_config.PageTitle)
        self.base_input(OneUnlock_config.PageTitle, values)

    # 选择开始时间
    def select_satrt_date(self):
        self.base_click(OneUnlock_config.StartDate)
        self.js_click_element(OneUnlock_config.NextMonth)
        self.base_click(OneUnlock_config.StartMark)
        self.base_click(OneUnlock_config.Schedule)

    # 选择结束时间
    def select_end_date(self):
        self.base_click(OneUnlock_config.EndDate)
        self.js_click_element(OneUnlock_config.NextMonth)
        self.js_click_element(OneUnlock_config.EndMark)
        self.base_click(OneUnlock_config.Schedule)

    # 分享链接预览图
    def share_link_image(self, values):
        self.base_input(OneUnlock_config.SelectImage, values)

    # 微信分享标题
    def wechat_share_title(self, values):
        self.base_input(OneUnlock_config.ShareTitle, values)

    # 微信分享描述
    def wechat_share_describe(self, values):
        self.base_input(OneUnlock_config.ShareDescribe, values)

    # 采集报名信息--"是"
    def collection_info(self):
        self.base_click(OneUnlock_config.SwitchYes)

    # 采集报名信息--"否"
    def nocollection_info(self):
        self.base_click(OneUnlock_config.SwitchNo)

    # 选择纯文本
    def select_palin_text(self):
        self.base_click(OneUnlock_config.PlainText)

    # 选择标题
    def select_title_module(self):
        self.base_click(OneUnlock_config.TitleModule)

    # 选择图文内容
    def select_graphic_content(self):
        self.base_click(OneUnlock_config.GraphicContent)

    # 纯文本-文字内容
    def Pt_verbal_content(self, values):
        self.base_clear(OneUnlock_config.VerbalContent)
        self.base_input(OneUnlock_config.VerbalContent, values)

    # 纯文本-链接地址
    def Pt_chain_address(self, values):
        self.base_input(OneUnlock_config.ChainAddress, values)

    # 标题-标题文字
    def Tm_title_text(self, values):
        self.base_input(OneUnlock_config.TitleText, values)

    # 图文内容-图片
    def Gc_select_image(self, values):
        self.base_input(OneUnlock_config.AddImage, values)

    # 图文内容-添加图片按钮
    def Gc_add_image(self):
        self.base_click(OneUnlock_config.AddImageButton)

    # 图文内容-删除按钮
    def Gc_delete_button(self):
        self.base_click(OneUnlock_config.GcSelectButton)

    # 图文内容-添加文字
    def Gc_add_character(self):
        self.base_click(OneUnlock_config.AddCharacter)

    # 图文内容-文案
    def Gc_copy_content(self, values):
        self.base_input(OneUnlock_config.GcopyContent, values)

    # 解锁奖励设置-商品名称
    def Uw_product_name(self, values):
        self.base_input(OneUnlock_config.ProductName, values)

    # 获取创建活动标题信息
    def get_create_activity_title(self):
        return self.base_get_text(OneUnlock_config.CreateActivityTitle)

    # 点击编辑
    def click_edit_button(self):
        self.click_tr_td_button_desc(OneUnlock_config.ActivityList, -1, -2)

    # 点击删除
    def click_delete_button(self):
        self.click_tr_td_button_desc(OneUnlock_config.ActivityList, -1, -1)

    # 点击复制活动
    def click_copy_activity_button(self):
        self.click_tr_td_button_desc(OneUnlock_config.ActivityList, -1, -3)

    # 点击分享
    def click_share_button(self):
        self.js_click_element(OneUnlock_config.ShareButton)

    # 点击查看详情
    def click_view_details_button(self):
        self.click_tr_td_button_desc(OneUnlock_config.ActivityList, -1, 0)

    # 确认删除
    def assert_delete(self):
        self.base_click(OneUnlock_config.AssertDelete)

    # 点击复制链接
    def click_copy_link(self):
        self.base_click(OneUnlock_config.CopyLinkButton)

    # 获取分享窗口标题信息
    def share_window_title_info(self):
        return self.base_get_text(OneUnlock_config.ShareInfo)

    # 点击活动数据
    def click_activity_data(self):
        self.base_click(OneUnlock_config.ActivityData)

    # 获取活动数据页面小标题
    def get_activity_data_title_info(self):
        return self.base_get_text(OneUnlock_config.VisitingNumber)

    # 点击用户详情
    def click_user_details(self):
        self.base_click(OneUnlock_config.UserDetails)

    # 获取用户详情表格信息
    def get_user_table_title(self, num):
        return self.get_tr_th(OneUnlock_config.GetUserTableTitle, num)

    # 点击预算分析
    def click_budget_analysis(self):
        self.base_click(OneUnlock_config.BudgetAnalysis)

    # 获取预算分析页面标题
    def get_budget_analysis_title(self):
        return self.base_get_text(OneUnlock_config.RedPocketPic)

    # 点击基本信息
    def click_basic_info(self):
        self.base_click(OneUnlock_config.BasicInfo)

    # 获取基本信息页面标题
    def get_basic_info_title(self):
        return self.base_get_text(OneUnlock_config.PageInformation)

    # 点击活动订单
    def click_activity_order(self):
        self.base_click(OneUnlock_config.ActivityOrder)

    # 获取活动订单表头信息
    def get_order_table_title(self, num):
        return self.get_tr_th(OneUnlock_config.ActivityOrderTable, num)

    # 进入我的活动
    def go_into_my_activity(self):
        self.base_click(OneUnlock_config.MyActivity)

    # 写入页面标题内容
    def write_page_title_content(self, content):
        self.base_clear(OneUnlock_config.PageTitle)
        self.base_input(OneUnlock_config.PageTitle, content)

    # 生成活动
    def success_create_activity(self):
        self.base_click(OneUnlock_config.FinishSetting)
        self.base_click(OneUnlock_config.AssertCreateActivity)
        self.base_click(OneUnlock_config.AssertAgain)

    # 获取提示信息
    def get_message_info(self):
        return self.base_get_text(OneUnlock_config.GetInfo)

    # 解锁奖励设置-商品介绍
    def Uw_product_itduction(self, values):
        self.base_input(OneUnlock_config.ProductItduction, values)

    # 解锁奖励设置-实际售价
    def Uw_actual_price(self, values):
        self.base_clear(OneUnlock_config.ActualPrice)
        self.base_input(OneUnlock_config.ActualPrice, values)

    # 解锁奖励设置-原价
    def Uw_original_price(self, values):
        self.base_input(OneUnlock_config.OriginalPrice, values)

    # 解锁奖励设置-库存数
    def Uw_quantity(self, values):
        self.base_input(OneUnlock_config.Quantity, values)

    # 解锁奖励设置-分销奖励
    def Uw_dstribution_rewards(self, values):
        self.base_input(OneUnlock_config.ShareWarding, values)

    # 解锁奖励设置-推荐好友报名
    def Uw_recommend_friends(self, values):
        self.base_input(OneUnlock_config.RecommendFriends, values)

    # 解锁奖励设置-奖励内容
    def Uw_reward_content(self, values):
        self.base_input(OneUnlock_config.RewardContent, values)

    # 解锁奖励设置_新增奖励
    def Um_add_reward(self):
        self.base_click(OneUnlock_config.AddReward)

    # 解锁奖励设置-删除
    def Um_delete_button(self):
        self.base_click(OneUnlock_config.DeleteButton)

    # 解锁奖励设置-第二阶奖励-推荐好友报名
    def Um_recommend_friends1(self, values):
        self.base_input(OneUnlock_config.RecommendFriends1, values)

    # 解锁奖励设置-第二阶奖励-奖励内容
    def Um_reward_content1(self, values):
        self.base_input(OneUnlock_config.RewardContent1, values)

    # 支付设置-购买后加微信-'是'
    def Wqr_switchyes(self):
        self.base_click(OneUnlock_config.PaySwitchYes)

    # 支付设置-购买后加微信-'否'
    def Wqr_switchno(self):
        self.base_click(OneUnlock_config.SwitchNo)

    # 支付设置-微信二维码
    def Wqr_wechat_scan(self, values):
        self.base_input(OneUnlock_config.WechatQR, values)

    # 支付设置-服务说明
    def Wqr_service_description(self, values):
        self.base_input(OneUnlock_config.ServiceDescription, values)

    # 海报设置-预览海报
    def Pt_poster_preview(self):
        self.base_click(OneUnlock_config.PtPreviewbutton)

    # 海报设置-海报预览按钮-海报预览字样
    def Pt_postpreview_text(self):
        return self.base_get_text(OneUnlock_config.PosterPreviewtext)

    # 海报设置-海报预览-关掉弹窗按钮
    def Pt_posterpreview_cancel(self):
        self.base_click(OneUnlock_config.PosterCancel)

    # 海报设置-复制推荐设置
    def Pt_copyrmend_setting(self, values):
        self.base_input(OneUnlock_config.CopyRmendcourse, values)

    # 报名信息设置-增加课程标签
    def If_add_labeling(self, values):
        self.base_input(OneUnlock_config.AddLabeling, values)

    # 报名信息设置-取消课程
    def If_cancel_course(self):
        self.base_click(OneUnlock_config.CourseCancel)

    # 新建成功
    def new_success(self):
        return self.base_get_text(OneUnlock_config.NewSuccess)

    # 活动列表第一条活动的标题
    def first_activity_title(self):
        return self.base_get_text(OneUnlock_config.FirstActivityName)

    # 获取活动主题名称
    def get_activity_name(self):
        return self.get_tr_td_desc(OneUnlock_config.ActivityList, 1)

    # 选择开始日期输入框
    def select_begin_input(self):
        self.base_click(OneUnlock_config.BeginTime)

    # 点击开始日期下一页
    def click_begin_next_page(self):
        self.base_click(OneUnlock_config.BeginNextPage)

    # 点击具体开始日期（下个月第一天）
    def click_begin_date(self):
        self.js_click_element(OneUnlock_config.BeginDateClick)

    # 确定开始日期
    def assert_begin_date(self):
        self.base_click(OneUnlock_config.BeginAssert)

    # 选择结束日期输入框
    def select_end_input(self):
        self.base_click(OneUnlock_config.EndTime)

    # 点击结束日期下一页
    def click_end_next_page(self):
        self.base_click(OneUnlock_config.EndNextPage)

    # 点击具体结束日期（下个月最后一天）
    def click_end_date(self):
        self.js_click_element(OneUnlock_config.EndDateClick)

    # 确定结束日期
    def assert_end_date(self):
        self.base_click(OneUnlock_config.EndAssert)
