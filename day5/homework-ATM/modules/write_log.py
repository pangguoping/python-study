#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther: pangguoping
import time
from modules import logger as modules_logger
def write_record(message,card_num):
    """
    账户记录
    :param message:
    :return:
    """
    struct_time = time.localtime()
    logger_obj = modules_logger.get_logger(card_num, struct_time)
    logger_obj.info(message)

