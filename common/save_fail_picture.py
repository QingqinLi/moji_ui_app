# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
import time


# unittest框架使用，pytest有conftest可以配置失败截图
def get_screen_shot(function):
    def inner(self, *args, **kwargs):
        try:
            result = function(self, *args, **kwargs)

            print("get_screen1", result)
            return result
        except Exception as e:
            print("get_screen", "error")
            stamp = str(int(time.time()))
            file_name = './static/picture_fail/' + function.__name__ + "_" + stamp + '_fail.png'
            print(file_name)
            self.driver.save_screenshot(file_name)
            raise AssertionError("断言异常")
        # try:
        #     result = function(self, *args, **kwargs)
        # except AssertionError:
        #     stamp = str(int(time.time()))
        #     file_name = './static/picture_fail/' + function.__name__ + "_"+stamp+'_fail.png'
        #     print(file_name)
        #     self.driver.save_screenshot(file_name)
    return inner