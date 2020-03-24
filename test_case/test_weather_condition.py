# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
from common.all_test import AllTest
from bussiness.weather_compare_bussiness import WeatherCompareBusiness
import unittest
from log.log import Logger
from common.save_fail_picture import get_screen_shot


class TestWeatherCondition(AllTest):

    def test_weather_desc_equal(self):
        self.weather_condition_business = WeatherCompareBusiness(self.driver)
        self.assertTrue(self.weather_condition_business.compare_weather())

    @get_screen_shot
    def test_temp_equal(self):
        self.weather_condition_business = WeatherCompareBusiness(self.driver)
        self.assertTrue(self.weather_condition_business.compare_temp())


if __name__ == '__main__':
    unittest.main()
