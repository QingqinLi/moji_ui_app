# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
import unittest
import time
import HTMLTestRunner


# 运行测试用例的入口
if __name__ == '__main__':
    test_dir = './test_case'
    suite = unittest.defaultTestLoader.discover(start_dir=test_dir, pattern='test_*.py')

    time_stamp = str(int(time.time()))
    report_path = './test_report/'+time_stamp+'.html'
    f = open(report_path, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='测试报告', description='测试首页和实况页面')
    runner.run(suite)
    f.close()
