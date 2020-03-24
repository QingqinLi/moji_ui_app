# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
import time


def get_screen_shot(function):
    def inner(self, *args, **kwargs):
        print("heello")
        try:
            function(self, *args, **kwargs)
        except AssertionError:
            stamp = str(int(time.time()))
            file_name = './static/picture_fail/' + function.__name__ + "_"+stamp+'_fail.png'
            print(file_name)
            self.driver.save_screenshot(file_name)
    return inner