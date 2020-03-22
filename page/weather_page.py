# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""


# 天气首页页面元素
class WeatherPage(object):

    def __init__(self, driver):
        self.driver = driver
        self.name = '123'

    def get_location(self):
        return self.driver.find_element_by_id("com.moji.mjweather:id/area_name_tv")

    def get_temperature(self):
        return self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.moji.mjweather:id/weather_info")')

    def get_condition(self):
        return self.driver.find_element_by_id("com.moji.mjweather:id/tv_weather_des")

    def get_condition_button(self):
        return self.driver.find_element_by_id("com.moji.mjweather:id/weather_info")

