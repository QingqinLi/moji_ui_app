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


class RunTest:
    def __init__(self):
        self.writecmd = WriteUserCommand()
        self.count = self.writecmd.get_file_lines()

    def add_test(self, i, l):
        l.accquire()
        test_dir = './test_case'
        suite = unittest.defaultTestLoader.discover(start_dir=test_dir, pattern='test_*.py')

        time_stamp = str(int(time.time()))
        report_path = './test_report/' + time_stamp + '.html'
        f = open(report_path, 'wb')
        runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='测试报告', description='测试首页和实况页面')
        runner.run(suite)
        f.close()
        l.release()

    def main(self):
        appium_list = []
        l = Lock()
        for i in range(self.count):
            ap = Thread(target=self.add_test, args=(i, l))
            appium_list.append(ap)
        [i.start() for i in appium_list]


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
