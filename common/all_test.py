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


class AllTest(unittest.TestCase):

    def __init__(self, i, methodName='runTest'):
        super(AllTest, self).__init__(methodName)
        self.i = i

    @classmethod
    def setUpClass(cls):
        cls.driver = BaseDriver().get_android_driver(cls.i)
        cls.driver.implicitly_wait(15)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        self.driver.launch_app()
        WebDriverWait(self.driver, 20, 1).until(EC.visibility_of(WeatherPage(self.driver).get_condition()))

    def tearDown(self):
        self.driver.close_app()

