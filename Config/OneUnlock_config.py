from selenium.webdriver.common.by import By

"""一元解锁活动配置数据"""
ModuleCenterClick = By.CSS_SELECTOR, '.menu-child-title', 1
OneUnlockClick = By.CSS_SELECTOR, '.activity-type .item', 3
ModuleInfo = By.CSS_SELECTOR, '.item-type', 0
ModuleClick = By.CSS_SELECTOR, '.temp-item', 0
ActivitySetting = By.CSS_SELECTOR, '.el-tabs__item', 0
ActivityPageSetting = By.CSS_SELECTOR, '.el-tabs__item', 1
UnlockWardingSetting = By.CSS_SELECTOR, '.el-tabs__item', 2
PaySetting = By.CSS_SELECTOR, '.el-tabs__item', 3
ShareWardingSetting = By.CSS_SELECTOR, '.el-tabs__item', 4
PosterSetting = By.CSS_SELECTOR, '.el-tabs__item', 5
InfoSetting = By.CSS_SELECTOR, '.el-tabs__item', 6
CancelButton = By.CSS_SELECTOR, '.el-button', 0
ReturnActivity = By.CSS_SELECTOR, '.el-button', 0
SetupComplete = By.CSS_SELECTOR, '.el-button', 4
SetupComplete1 = By.CSS_SELECTOR, '.el-button', 2
SetupComplete2 = By.CSS_SELECTOR, '.el-button', 5
ConfirmButton = By.CSS_SELECTOR, '.el-button', 5
ClosePopup = By.CSS_SELECTOR, '.el-message-box__close', 0
'''活动设置配置数据'''
StartDate = By.CSS_SELECTOR, '.el-input--suffix .el-input__inner', 0
NextMonth = By.CSS_SELECTOR, '.el-date-picker__header .el-icon-arrow-right', -1
StartMark = By.CSS_SELECTOR, '.available', 0
EndMark = By.CSS_SELECTOR, '.el-date-table .available', -1
# Schedule=By.CSS_SELECTOR,'.el-button--mini.is-round',0
Schedule = By.CSS_SELECTOR, '.page-config-editor .field-label', 1
EndDate = By.CSS_SELECTOR, '.el-input--suffix .el-input__inner', 1
SelectImage = By.CSS_SELECTOR, '.el-upload__input', 0
ShareTitle = By.CSS_SELECTOR, '.fe-text .el-input__inner', 1
ShareDescribe = By.CSS_SELECTOR, '.fe-text .el-input__inner', 2
SwitchYes = By.CSS_SELECTOR, '.el-radio__inner', 0
SwitchNo = By.CSS_SELECTOR, '.el-radio__inner', 1
'''活动页面设置配置数据'''
PlainText = By.CSS_SELECTOR, '.add-block-btn', 0
TitleModule = By.CSS_SELECTOR, '.add-block-btn', 1
GraphicContent = By.CSS_SELECTOR, '.add-block-btn', 2
'''纯文本'''
VerbalContent = By.CSS_SELECTOR, '.w-e-text', 0
ChainAddress = By.CSS_SELECTOR, '.el-input__inner', 6
'''标题'''
TitleText = By.CSS_SELECTOR, '.el-input__inner', 6
'''图文内容'''
AddImageButton = By.CSS_SELECTOR, '.add-btn', 0
AddImage = By.CSS_SELECTOR, '.el-upload .el-upload__input', 1
AddCharacter = By.CSS_SELECTOR, '.add-btn', 1
GcSelectButton = By.CSS_SELECTOR, '.delete-btn', 0
GcopyContent = By.CSS_SELECTOR, '.w-e-text', 0
'''解锁奖励设置页配置数据'''
ProductName = By.CSS_SELECTOR, '.el-input__inner', 6
ProductItduction = By.CSS_SELECTOR, '.el-input__inner', 7
ActualPrice = By.CSS_SELECTOR, '.el-input__inner', 8
OriginalPrice = By.CSS_SELECTOR, '.el-input__inner', 9
Quantity = By.CSS_SELECTOR, '.el-input__inner', 10
ShareWarding = By.CSS_SELECTOR, '.el-input__inner', 11
RecommendFriends = By.CSS_SELECTOR, '.el-input__inner', 12
RewardContent = By.CSS_SELECTOR, '.el-textarea__inner', 0
AddReward = By.CSS_SELECTOR, '.el-icon-plus', 0
DeleteButton = By.CSS_SELECTOR, '.el-icon-delete', 0
RecommendFriends1 = By.CSS_SELECTOR, '.el-input__inner', 13
RewardContent1 = By.CSS_SELECTOR, '.el-textarea__inner', 1
'''支付设置页配置数据'''
PaySwitchYes = By.CSS_SELECTOR, '.el-radio__inner', 2
WechatQR = By.CSS_SELECTOR, '.el-upload__input', 1
ServiceDescription = By.CSS_SELECTOR, '.ql-editor', 0
'''分享奖励设置页配置数据'''
UserShare = By.CSS_SELECTOR, '.el-checkbox__label', 0
BringStudents = By.CSS_SELECTOR, '.el-checkbox__label', 1
UserRecommed = By.CSS_SELECTOR, '.el-checkbox__label', 2
'''海报设置页配置数据'''
PtPreviewbutton = By.CSS_SELECTOR, '.preview-btn', 0
CopyRmendcourse = By.CSS_SELECTOR, '.el-input__inner', 13
PosterCancel = By.CSS_SELECTOR, '.el-dialog__close', 0
PosterPreviewtext = By.CSS_SELECTOR, '.el-dialog__header', 0
'''报名信息设置页配置数据'''
AddLabeling = By.CSS_SELECTOR, '.el-button', 3
CourseCancel = By.CSS_SELECTOR, '.el-tag__close', 0
NewSuccess = By.CSS_SELECTOR, '.el-message', 0
FirstActivityName = By.CSS_SELECTOR, '.cell', 9
CreateActivityTitle = By.CSS_SELECTOR, '.bottom .nav-item', 1

# 基于活动列表的操作元素
ActivityList = By.CSS_SELECTOR, '.el-table__body-wrapper.is-scrolling-none', 0
AssertDelete = By.CSS_SELECTOR, '.el-message-box .el-button--small', 1
ShareButton = By.CSS_SELECTOR, '.operate-btn.success-btn', 0
ShareInfo = By.CSS_SELECTOR, '.el-popover .activity-title', 0
CopyLinkButton = By.CSS_SELECTOR, '.copy-btn', -1
ActivityData = By.CSS_SELECTOR, '.el-tabs__item', 0
UserDetails = By.CSS_SELECTOR, '.el-tabs__item', 1
BudgetAnalysis = By.CSS_SELECTOR, '.el-tabs__item', 2
BasicInfo = By.CSS_SELECTOR, '.el-tabs__item', 3
ActivityOrder = By.CSS_SELECTOR, '.el-tabs__item', 4
VisitingNumber = By.CSS_SELECTOR, '.charts-list .title', 0
GetUserTableTitle = By.CSS_SELECTOR, '.el-table__header', 0
RedPocketPic = By.CSS_SELECTOR, '.trend-title', 0
PageInformation = By.CSS_SELECTOR, '.head-title', 0
ActivityOrderTable = By.CSS_SELECTOR, '.el-table__header', 0
MyActivity = By.CSS_SELECTOR, '.menu-child-title', 0
PageTitle = By.CSS_SELECTOR, '.el-input__inner', 0
FinishSetting = By.CSS_SELECTOR, '.el-button--primary', 1
AssertCreateActivity = By.CSS_SELECTOR, '.el-button--primary', 2
AssertAgain = By.CSS_SELECTOR, '.el-message-box .el-button--primary', 0
GetInfo = By.CSS_SELECTOR, '.el-message.el-message--success', 0
# 选择日期
BeginTime = By.CSS_SELECTOR, '.el-date-editor--datetime', 0
EndTime = By.CSS_SELECTOR, '.el-date-editor--datetime', 1
BeginNextPage = By.CSS_SELECTOR, '.el-picker-panel__body .el-date-picker__header .el-icon-arrow-right', 0
EndNextPage = By.CSS_SELECTOR, '.el-picker-panel__body .el-date-picker__header .el-icon-arrow-right', 1
BeginDateClick = By.CSS_SELECTOR, '.el-date-table .available', 0
EndDateClick = By.CSS_SELECTOR, '.el-date-table .available', -1
BeginAssert = By.CSS_SELECTOR, '.el-button--mini.is-plain', 1
EndAssert = By.CSS_SELECTOR, '.el-button--mini.is-plain', 2
