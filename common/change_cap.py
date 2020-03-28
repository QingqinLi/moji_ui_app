# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
from app_config import desired_cap
from app_config import port_mes


# 修改app配置参数
class ChangeParam:

    def change_desired_cap(self, device_name, p):
        desired_cap['deviceName'] = device_name
        port_mes['port'] = p

    def get_desired_cap(self):
        return desired_cap


# if __name__ == '__main__':
#     ch = ChangeParam(
#     print(ch.get_desired_cap())