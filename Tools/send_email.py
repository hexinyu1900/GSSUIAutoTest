# 需要使用到SMTPLIB库，来进行邮箱的连接
import smtplib
# 处理邮件内容的库，email.mime
from email import encoders
from email.mime.text import MIMEText
# 处理邮件附件，需要导入MIMEMultipart，Header，MIMEBase
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.base import MIMEBase
from Config.Env_config import *


def send_email(report_dir):

    # 邮件中发送附件
    # 附件配置邮箱
    email = MIMEMultipart()
    content = '好生源UI自动化测试报告，详情见附件'
    email.attach(MIMEText(content, 'plain', 'utf-8'))  # 纯文本形式的邮件内容的定义，通过MIMEText进行操作
    email['Subject'] = 'GSS-自动化测试报告'  # 定义邮件主题
    email['From'] = userName_SendMail  # 发件人
    email['To'] = ','.join(received_mail)  # 收件人

    # 非图片附件
    att = MIMEBase('application', 'octet-stream')
    att.set_payload(open(report_dir, 'rb').read())
    att.add_header('Content-Disposition', 'attachment', filename=Header('GSS-UI自动化测试报告.html', 'gbk').encode())
    encoders.encode_base64(att)
    email.attach(att)

    # 发送邮件
    smtp = smtplib.SMTP_SSL(mail_server, port=465)  # 非QQ邮箱，一般使用SMTP即可，不需要有SSL
    smtp.login(userName_SendMail, userName_AuthCode)
    smtp.sendmail(userName_SendMail, ','.join(received_mail), email.as_string())
    smtp.quit()

#
# class SendEmail:
#
#     @staticmethod
#     def send_email(report_dir):
#         # 邮箱属性配置
#         mail_server = 'smtp.qq.com'  # 邮箱服务端URL
#         userName_SendMail = '1748629301@qq.com'  # 发件人/用户名
#         userName_AuthCode = 'cqksvavcotkaeceg'  # 邮箱发件授权码
#         received_mail = ['1297560025@qq.com']  # 定义邮件的接收者
#
#         # 邮件中发送附件
#         # 附件配置邮箱
#         email = MIMEMultipart()
#         content = '好生源UI自动化测试报告，详情见附件'
#         email.attach(MIMEText(content, 'plain', 'utf-8'))  # 纯文本形式的邮件内容的定义，通过MIMEText进行操作
#         email['Subject'] = 'GSS-自动化测试报告'  # 定义邮件主题
#         email['From'] = userName_SendMail  # 发件人
#         email['To'] = ','.join(received_mail)  # 收件人
#
#         # 非图片附件
#         att = MIMEBase('application', 'octet-stream')
#         att.set_payload(open(report_dir, 'rb').read())
#         att.add_header('Content-Disposition', 'attachment', filename=Header('GSS-UI自动化测试报告.html', 'gbk').encode())
#         encoders.encode_base64(att)
#         email.attach(att)
#
#         # 发送邮件
#         smtp = smtplib.SMTP_SSL(mail_server, port=465)  # 非QQ邮箱，一般使用SMTP即可，不需要有SSL
#         smtp.login(userName_SendMail, userName_AuthCode)
#         smtp.sendmail(userName_SendMail, ','.join(received_mail), email.as_string())
#         smtp.quit()
