# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
# app配置


class AppParam:

    @staticmethod
    def get_desired_cap(device_name):
        desired_cap = {
            "platformName": "Android",
            "app": "/Users/qing.li/Downloads/moji822.apk",
            "noReset": True,
            "deviceName": device_name,
            "appActivity": "com.moji.mjweather.MainActivity",
            "unicodeKeyboard": True,
            "resetKeyboard": True,
            "noSign": True,
        }
        return desired_cap
