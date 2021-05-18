import unittest
import time
from Tools.send_email import send_email
from Tools.HTMLTestRunner import HTMLTestRunner
from Test.CaseSuite.case_suite import CaseSuite
from Tools.webhook import web_hook
from Config.Env_config import *

suite = CaseSuite().case_suite()

# 获取报告文件流并执行
with open(report_dir, 'wb') as f:
    Runner = HTMLTestRunner(stream=f, verbosity=2, title=title, description=Browser).run(suite)

if Send:
    # 发送邮件
    send_email(report_dir)

    # 钉钉推送
    web_hook(
        '版本号：{}\n测试环境：{}\n浏览器：{}Browser\nUI自动化测试任务结束啦，快去邮箱查看测试报告吧!\
        \n运行总数：{}\n成功数量：{}\n失败数量：{}\n错误数量：{}\n跳过数量：{}'.format(
            version, env, Browser, len(Runner.result), Runner.success_count, Runner.failure_count, Runner.error_count, Runner.skip_count
        ),
        phone
    )
else:
    pass

# runner = unittest.TextTestRunner()
# runner.run(suite)
