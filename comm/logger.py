# coding: utf-8
# author: chengmo
# description:

"""
日志模块: 封装日志模板
"""

import os
import sys
from loguru import logger
from conf import config


def init():
    """初始化日志"""
    # 移除默认处理器
    logger.remove()

    # 创建文件处理器, 按大小滚动归档, 保留最近10个日志文件
    log_file = config.get_log_file()
    log_dir = os.path.dirname(log_file)
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    logger.add(
        log_file,
        rotation=config.get_log_max_size(),
        retention=config.get_log_backup_count(),
        level=config.get_log_level(),
        format=config.get_log_format(),
        encoding="utf-8",
    )

    # 配置控制台输出，调试时显示DEBUG级别信息
    logger.add(
        sys.stderr,
        level="DEBUG",
        format=config.get_log_format(),
    )


def debug(message):
    """记录调试日志"""
    logger.debug(message)


def info(message):
    """记录信息日志"""
    logger.info(message)


def warning(message):
    """记录警告日志"""
    logger.warning(message)


def error(message):
    """记录错误日志"""
    logger.error(message)


def critical(message):
    """记录严重错误日志"""
    logger.critical(message)

