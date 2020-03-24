# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
from util.command import Command
from util.port import Port
from util.write_user_command import WriteUserCommand
import threading
# 开启appium服务器


class Server:
    def __init__(self):
        self.cmd = Command()
        self.port = Port()
        self.writecmd = WriteUserCommand()
        self.devices = self.get_devices()

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

    def create_server_list(self):
        command_list = []
        appium_port_list = self.get_port(4800)
        bootstrap_port_list = self.get_port(4900)
        for i in range(len(self.devices)):
            command = "appium -p " + str(appium_port_list[i]) + " -bp " + str(bootstrap_port_list[i]) + \
                " -U " + str(self.devices[i]) + " --no-reset --session-override --log ../log/logs/appium.log"
            command_list.append(command)
            self.writecmd.write_data(i, self.devices[i], appium_port_list[i], bootstrap_port_list[i])
            # 把port和devices的对应关系写进配置文件中去
        return command_list

    def start_server(self, i):
        """
        开启appium服务
        :return:
        """
        appium_command = self.create_server_list()[i]
        print("appium_command", appium_command)
        self.cmd.execute_cmd(appium_command)

    def kill_server(self):
        # 查看当前node服务器是否有相应进程
        server_list = self.cmd.execute_cmd("ps -ef | grep node")
        if server_list:
            self.cmd.execute_cmd("killall node")

    def main(self):
        """
        多线程启动appim
        :return:
        """
        self.kill_server()
        self.writecmd.clear_data()
        appium_list = []
        for i in range(len(self.devices)):
            appium_t = threading.Thread(target=self.start_server, args=(i,))
            appium_list.append(appium_t)
        [i.start() for i in appium_list]


if __name__ == '__main__':
    s = Server()
    print(s.main())



