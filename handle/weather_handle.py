# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
from page.weather_page import WeatherPage
from page.condition_page import ConditionPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction
import time

# 操作weather页面的元素
class WeatherHandle:
    def __init__(self, driver):
        self.driver = driver
        self.weather_page = WeatherPage(driver=driver)
        self.condition_page = ConditionPage(driver=driver)
        self.touch_action = TouchAction(self.driver)

    def get_location_text(self):
        return self.weather_page.get_location().text

    def get_temperature_text(self):
        return self.weather_page.get_temperature().text

    def get_weather_desc(self):
        return self.weather_page.get_condition().text

    def click_condition_area(self):
        time.sleep(1)
        self.touch_action.tap(self.weather_page.get_condition_button()).perform()
        time.sleep(2)
        WebDriverWait(self.driver, 20, 0.5).until(EC.visibility_of(self.condition_page.get_condition_weather()))

