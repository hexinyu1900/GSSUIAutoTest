
# 测试环境浏览器地址
env = "dev"
url = "https://gssdev.haoshengy.com/pc_workbench/login"

# 版本号
version = "GSS-v1.4.2"

# 定义报告存放路径及文件名称
report_dir = 'E:\Gss_UI_AutoTest\Report\GSS-自动化测试报告.html'

# 定义邮件标题
title = "GSS-自动化测试报告"
Browser = "Chrome"

# 定义邮件配置
mail_server = 'smtp.qq.com'  # 邮箱服务端URL
userName_SendMail = '1748629301@qq.com'  # 发件人/用户名
userName_AuthCode = 'cqksvavcotkaeceg'  # 邮箱发件授权码
received_mail = ['1297560025@qq.com']  # 定义邮件的接收者

# 钉钉推送
web_hook_url = "https://oapi.dingtalk.com/robot/send?access_token=c3c57aede4e232ebaf322ea0c092b96df46a90fb9bec85448ac59197d77953ad"
phone = ["18113748898"]

# 照片存放路径
image_path=r'E:\Gss_UI_AutoTest\Image'

# 判断是否发送邮件和推送
# Send = True  # 发送
Send = False  # 不发送
