# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
import yaml
import os
from config.setting import Base_DIR


class WriteUserCommand:
    def __init__(self):
        self.path = os.path.join(Base_DIR, "config/userconfig.yaml")

    def get_data(self):
        """
        加载文件
        :return:
        """
        with open(self.path) as f:
            data = yaml.full_load(f)
            return data

    def write_data(self, i, device_name, port, bp):
        data = self.join_data(i, device_name, port, bp)
        with open(self.path, 'a+') as f:
            yaml.dump(data, f)

    def get_value(self, section, key):
        data = self.get_data()
        return data["user_info_"+str(section)][key]

    def join_data(self, i, device_name, port, bp):
        data = {
            "user_info_"+str(i): {
                "device_name": device_name,
                "port": port,
                "bp": bp
            }
        }
        return data

    def clear_data(self):
        with open(self.path, 'w') as f:
            f.truncate()

    def get_file_lines(self):
        data = self.get_data()
        if data:
            return len(data)
        else:
            return 0


# if __name__ == '__main__':
#     wr = WriteUserCommand()
#     print(wr.get_value(0, "device_name"))

