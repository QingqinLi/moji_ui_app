# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""


class ConditionPage:
    def __init__(self, driver):
        self.driver = driver

    def get_condition_temp(self):
        return self.driver.find_element_by_id("com.moji.mjweather:id/wc_weather_tmp")

    def get_condition_weather(self):
        return self.driver.find_element_by_id("com.moji.mjweather:id/wc_weather_desc")
        # return self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.moji.mjweather:id/wc_weather_desc")')
