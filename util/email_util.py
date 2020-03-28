# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
import smtplib
from email.mime.text import MIMEText
from email.header import Header


class EmailUtil:

    sender = "1589369708@qq.com"
    receivers = 'qing.li@moji.com,13263106808@163.com'
    smtpserver = 'smtp.qq.com'
    username = '1589369708@qq.com'
    # 第三方使用授权码登录
    password = 'fbgsrzbjtxlgffag'

    # 邮件主题
    mail_title = 'android-ui自动化测试报告'

    def send_email(self, path):
        # 读取报告文件
        with open(path, 'rb') as f:
            mail_file = f.read()
        # 邮件内容，格式，编码
        message = MIMEText(mail_file, 'html', 'utf-8')
        # 指定邮件的收发件人，标题
        message['From'] = self.sender
        message['To'] = self.receivers
        message['Subject'] = Header(self.mail_title, 'utf-8')

        try:
            smtp = smtplib.SMTP_SSL("smtp.qq.com", 465)
            # smtp.connect(self.smtpserver, 465)
            smtp.login(self.username, self.password)
            smtp.sendmail(self.sender, self.receivers.split(','), message.as_string())
            smtp.quit()
            print("邮件发送成功！！！")
        except smtplib.SMTPException as e:
            print("邮件发送失败", path, e)


if __name__ == '__main__':
    file_path = '/Users/qing.li/PycharmProjects/moji_ui_app/test_report/report_html/1585151572_R58MB0Z4WCX.html'
    email = EmailUtil()
    email.send_email(file_path)



