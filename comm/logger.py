# coding: utf-8
# author: chengmo
# description:

"""
日志模块: 封装日志模板
"""

import os
import logging
from logging.handlers import RotatingFileHandler
from conf import config

# 全局日志对象
logger = None

def init():
    """初始化日志"""
    global logger
    
    # 创建日志对象
    logger = logging.getLogger('test-frame')
    
    # 设置日志级别
    level = getattr(logging, config.get_log_level().upper())
    logger.setLevel(level)
    
    # 创建日志格式
    formatter = logging.Formatter(config.get_log_format())
    
    # 创建控制台处理器
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    # 创建文件处理器
    log_file = config.get_log_file()
    log_dir = os.path.dirname(log_file)
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
        
    file_handler = RotatingFileHandler(
        log_file,
        maxBytes=config.get_log_max_size(),
        backupCount=config.get_log_backup_count(),
        encoding='utf-8'
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

def debug(message):
    """记录调试日志"""
    if logger:
        logger.debug(message)

def info(message):
    """记录信息日志"""
    if logger:
        logger.info(message)

def warning(message):
    """记录警告日志"""
    if logger:
        logger.warning(message)

def error(message):
    """记录错误日志"""
    if logger:
        logger.error(message)

def critical(message):
    """记录严重错误日志"""
    if logger:
        logger.critical(message)