# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
import unittest
import time
import HTMLTestRunner
from util.write_user_command import WriteUserCommand
from threading import Thread, Lock
import pytest
from config.setting import Base_DIR
from common.change_cap import ChangeParam
from util.start_appium_server import Server
from app_config import rerun
from util.command import Command
from util.email_util import EmailUtil


class RunTest:
    def __init__(self):
        self.writecmd = WriteUserCommand()
        self.change_des = ChangeParam()
        self.server = Server()
        self.command = Command()
        self.email = EmailUtil()

    def add_test(self, i):
        print("第{}个线程开始执行".format(i))
        # l.acquire()

        # test_dir = './test_case'
        # suite = unittest.defaultTestLoader.discover(start_dir=test_dir, pattern='test_*.py')
        #
        # time_stamp = str(int(time.time()))
        # report_path = './test_report/' + time_stamp + '.html'
        # f = open(report_path, 'wb')
        # runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='测试报告', description='测试首页和实况页面')
        # runner.run(suite)
        # f.close()

        # pytest运行
        # 读取配置文件，获取devices_name和port
        device_name = self.writecmd.get_value(i, "device_name")
        port = self.writecmd.get_value(i, "port")
        self.change_des.change_desired_cap(device_name, port)
        test_dir = './test_case'
        time_stamp = str(int(time.time()))
        html_report = Base_DIR + '/test_report/report_html/' + time_stamp + '_' + device_name + '.html'
        xml_report = Base_DIR + '/test_report/xml_report/' + time_stamp + '_' + device_name + '.xml'
        allure_reports = Base_DIR+'/test_report/allure_reports_'+device_name
        # cmd_clean = "allure generate "+allure_reports+"/ --clean"
        # print("cmd_clean", cmd_clean)
        # self.command.execute_cmd(cmd_clean)
        allure_report = Base_DIR + '/test_report/report_'+device_name+'/html/'
        pytest.main(["-s", "-v", test_dir,
                     "--html="+html_report,
                     # "--junit-xml="+xml_report,
                     "--self-contained-html",
                     "--alluredir="+allure_reports,
                     "--reruns", rerun])
        # 报告集成使用jenkins的allure包完成
        # cmd = "allure generate "+allure_reports+" -o "+allure_report + " --clean"
        # 等待3s，确保html报告生成成功
        time.sleep(3)
        self.email.send_email(html_report)
        # self.command.execute_cmd(cmd)
        print("第{}个线程结束执行".format(i))

        # l.release()

    def main(self):
        self.server.start()
        time.sleep(5)
        count = self.writecmd.get_file_lines()
        # appium_list = []
        # l = Lock()
        for i in range(count):
            ap = Thread(target=self.add_test, args=(i, ))
            # appium_list.append(ap)
            ap.start()
            time.sleep(5)
        # [i.start() for i in appium_list]


# 运行测试用例的入口
if __name__ == '__main__':
    runner = RunTest()
    runner.main()
    # test_dir = './test_case'
    # suite = unittest.defaultTestLoader.discover(start_dir=test_dir, pattern='test_*.py')
    #
    # time_stamp = str(int(time.time()))
    # report_path = './test_report/'+time_stamp+'.html'
    # f = open(report_path, 'wb')
    # runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='测试报告', description='测试首页和实况页面')
    # runner.run(suite)
    # f.close()close
