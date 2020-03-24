# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
from appium import webdriver
from app_config import AppParam
from util.write_user_command import WriteUserCommand


class BaseDriver:
    def __init__(self):
        self.app_param = AppParam()
        self.writeusercommand = WriteUserCommand()

    def get_android_driver(self, i):
        device_name = self.writeusercommand.get_value("user_info_"+str(i), "device_name")
        port = self.writeusercommand.get_value("user_info_"+str(i), "port")
        bp = self.writeusercommand.get_value("user_info_"+str(i), "bp")
        desried_cap = self.app_param.get_desired_cap(device_name)
        driver = webdriver.Remote("http://127.0.0.1:"+str(port)+"wd/hub", desried_cap)
        return driver

    def get_ios_driver(self):
        pass