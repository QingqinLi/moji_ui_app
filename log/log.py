# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
import logging
from common.setting import DEBUG


class Logger:
    def __init__(self, file_name):
        log_path = './log/logs/' + file_name + '.log'
        self.logger = logging.getLogger()
        fh = logging.FileHandler(log_path, encoding='utf-8')
        sh = logging.StreamHandler()
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(lineno)d - %(levelname)s - %(message)s")
        # formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        fh.setFormatter(formatter)
        sh.setFormatter(formatter)
        self.logger.addHandler(fh)
        self.logger.addHandler(sh)
        if DEBUG:
            self.logger.setLevel(logging.INFO)
        else:
            self.logger.setLevel(logging.WARNING)
        # self.logger.removeHandler(fh)
        # self.logger.removeHandler(sh)
        fh.close()
        sh.close()

    def get_logger(self):
        return self.logger

