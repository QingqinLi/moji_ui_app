# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
from util.command import Command
from util.port import Port
from util.write_user_command import WriteUserCommand
import threading
from threading import Lock
import time
# 开启appium服务器


class Server:
    def __init__(self):
        self.cmd = Command()
        self.port = Port()
        self.writecmd = WriteUserCommand()
        self.devices = self.get_devices()
        self.appium_port_list = self.get_port(4800)
        self.bootstrap_port_list = self.get_port(4900)

    def get_devices(self):
        """
        获取连接的移动设备
        :return:
        """
        result = self.cmd.execute_command_result("adb devices")
        devices_list = []
        for i in result:
            if i == 'List of devices attached':
                continue
            devices_list.append(i.replace("\tdevice", ""))
        return devices_list

    def get_port(self, start_port):
        port_list = self.port.create_port_list(start_port, len(self.devices))
        return port_list

    def create_server_list(self, i):
        command = "appium -p " + str(self.appium_port_list[i]) + " -bp " + str(self.bootstrap_port_list[i]) + \
            " -U " + str(self.devices[i]) + " --no-reset --session-override --log ../log/logs/appium.log"
        self.writecmd.write_data(i, self.devices[i], self.appium_port_list[i], self.bootstrap_port_list[i])
        # 把port和devices的对应关系写进配置文件中去
        return command

    def start_server(self, i, l):
        """
        开启appium服务
        :return:
        """
        l.acquire()
        appium_command = self.create_server_list(i)
        self.cmd.execute_cmd(appium_command)
        l.release()

    def kill_server(self):
        # 查看当前node服务器是否有相应进程
        server_list = self.cmd.execute_command_result("ps -ef | grep node")
        if server_list:
            self.cmd.execute_cmd("killall node")
        time.sleep(2)

    def start(self):
        """
        多线程启动appim
        :return:
        """
        self.kill_server()
        self.writecmd.clear_data()
        appium_list = []
        l = Lock()
        for i in range(len(self.devices)):
            appium_t = threading.Thread(target=self.start_server, args=(i, l))
            appium_list.append(appium_t)
        [i.start() for i in appium_list]


# if __name__ == '__main__':
#     s = Server()
#     print(s.start())



