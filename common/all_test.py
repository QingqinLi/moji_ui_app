# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
import unittest
from appium import webdriver
# from app_config import desired_cap
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page.weather_page import WeatherPage
from common.basedriver import BaseDriver


class AllTest:

    # @classmethod
    # def setup_class(cls):
    #     cls.driver = BaseDriver().get_android_driver()
    #     cls.driver.implicitly_wait(15)
    #
    # @classmethod
    # def teardown_class(cls):
    #     cls.driver.quit()

    def setup(self):
        self.driver.launch_app()
        WebDriverWait(self.driver, 20, 1).until(EC.visibility_of(WeatherPage(self.driver).get_condition()))

    def teardown(self):
        self.driver.close_app()

