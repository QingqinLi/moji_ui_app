# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
from common.all_test import AllTest
from bussiness.weather_compare_bussiness import WeatherCompareBusiness
import pytest
import allure
from app_config import desired_cap
from log.log import Logger
from common.save_fail_picture import get_screen_shot
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page.weather_page import WeatherPage


class TestWeatherCondition:

    # def setup(self):
    #     browser.launch_app()
    # #     WebDriverWait(self.driver, 20, 1).until(EC.visibility_of(WeatherPage(self.driver).get_condition()))
    #
    # def teardown(self):
    #     browser.close_app()
    device_name = desired_cap['deviceName']

    @classmethod
    def teardown_class(cls):
        print('hihihihi')

    # @pytest.mark.skip
    @allure.suite("123")
    @allure.title("test_weather_desc_equal_" + device_name)
    def test_weather_desc_equal(self, browser):
        """
        judge weather_desc in main page and condition page
        :param browser:
        :return:
        """
        self.weather_condition_business = WeatherCompareBusiness(browser)
        print("hello")
        assert self.weather_condition_business.compare_weather()

    # @pytest.mark.flaky(reruns=1, reruns_delay=1)
    # @pytest.mark.skip
    @allure.title("test_temp_equal_"+device_name)
    @allure.story("hello")
    def test_temp_equal(self, browser):
        self.weather_condition_business = WeatherCompareBusiness(browser)
        result = self.weather_condition_business.compare_temp()
        assert result


if __name__ == '__main__':
    pytest.main()
