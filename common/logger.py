# coding:utf-8
import logging
import os
import time

path = 'D:\\testinterfaceProject'


def get_log(logger_name):
    # 创建ogger输出日志对象
    logger = logging.getLogger(logger_name)
    # 设置最低日志级别：分别低到高有debug、info、warning、error以及critical
    logger.setLevel(level=logging.INFO)
    # 设置日志存放路径，日志文件名
    # 设置所有日志和错误日志的存放路径
    all_log_path = os.path.join(path, 'log/')
    # 设置日志文件名
    ctime = time.strftime("%Y-%m-%d_%H_%M_%S", time.localtime())
    all_log_name = all_log_path + ctime + '.log'
    all_handler = logging.FileHandler(all_log_name, encoding='utf-8')
    # 指定被处理的信息级别，低于设置级别的信息将被忽略
    all_handler.setLevel(logging.DEBUG)
    # 创建一个handler输出到控制台
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    # 设置输出日志格式
    # 以时间-日志器名称-日志级别-日志内容的形式展示
    all_log_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(module)s  - %(lineno)s - %('
                                          'message)s')
    # 以时间-日志器名称-日志级别-文件名-函数行号-错误内容
    # 给handler添加输出的日志格式
    all_handler.setFormatter(all_log_formatter)
    # error_handler.setFormatter(error_log_formatter)
    console_handler.setFormatter(all_log_formatter)
    # 给logger添加handler
    logger.addHandler(all_handler)
    # logger.addHandler(error_handler)
    logger.addHandler(console_handler)
    return logger
