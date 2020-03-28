# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
# 执行操作系统命令
import os
import subprocess
from config.setting import Base_DIR


class Command:

    @staticmethod
    def execute_command_result(cmd):
        # 执行有返回结果的命令
        result_list = []
        result = os.popen(cmd).readlines()
        for i in result:
            # 按行读，结尾会有\n
            if i == '\n':
                continue
            result_list.append(i.strip('\n'))
        return result_list

    @staticmethod
    def execute_cmd(cmd):
        log_path = os.path.join(Base_DIR + "/log/logs/appium_log.log")
        # print(Base_DIR, log_path)
        subprocess.Popen(cmd, shell=True, stdout=open(log_path, 'a'), stderr=subprocess.STDOUT)


if __name__ == '__main__':
    command = Command()
    print(command.execute_command_result("ls"))