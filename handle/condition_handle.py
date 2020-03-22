# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
from page.condition_page import ConditionPage


# 操作实况页面的元素
class ConditionHandle:
    def __init__(self, driver):
        self.condition_page = ConditionPage(driver)

    def get_temperature_text(self):
        return self.condition_page.get_condition_temp().text

    def get_weather_text(self):
        return self.condition_page.get_condition_weather().text

