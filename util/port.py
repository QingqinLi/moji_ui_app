# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
from util.command import Command


# 生成备用端口,不能是正在使用的端口
class Port:
    def __init__(self):
        self.cmd = Command()

    def port_is_used(self, port):
        result = self.cmd.execute_command_result("netstat -nat | grep " + str(port))
        if len(result) > 0:
            return True
        else:
            return False

    def create_port_list(self, start_port, port_num):
        """
        生成可用端口
        :param start_port:
        :param device_list:
        :return:
        """
        port_list = []
        port = start_port
        for i in range(port_num):
            port += 1
            while True:
                if not self.port_is_used(port) and port <= 65535:
                    port_list.append(port)
                    break
                port += 1
        return port_list


if __name__ == '__main__':
    port = Port()
    print(port.create_port_list(4740, 4))







