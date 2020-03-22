# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
# 验证首页的天气信息和实况页面的天气信息是否一致
from handle.condition_handle import ConditionHandle
from handle.weather_handle import WeatherHandle


class WeatherCompareBusiness:
    def __init__(self, driver):
        self.driver = driver
        self.weather_handle = WeatherHandle(driver)
        self.condition_handle = ConditionHandle(driver)

    def compare_weather(self):
        weather_desc = self.weather_handle.get_weather_desc()
        print(weather_desc)
        self.weather_handle.click_condition_area()
        condition_desc = self.condition_handle.get_weather_text()
        print(condition_desc)
        return weather_desc == condition_desc

    def compare_temp(self):
        weather_temp = self.weather_handle.get_temperature_text()
        self.weather_handle.click_condition_area()
        condition_temp = self.condition_handle.get_temperature_text()
        print(weather_temp, condition_temp)
        return weather_temp == condition_temp
