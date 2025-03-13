# coding: utf-8
# author: chengmo
# description:

"""
配置模块: 读取config.ini
"""

import os
import configparser
from datetime import datetime

# 配置文件路径
CONFIG_FILE = os.path.join(os.path.dirname(__file__), 'config.ini')

# 全局配置对象
_config = None

def init():
    """初始化配置"""
    global _config
    _config = configparser.ConfigParser()
    
    # 检查配置文件是否存在
    if os.path.exists(CONFIG_FILE):
        _config.read(CONFIG_FILE, encoding='utf-8')
    else:
        raise FileNotFoundError(f"配置文件不存在: {CONFIG_FILE}")

def get_smtp_server():
    """获取SMTP服务器地址"""
    return _config.get('smtp', 'server')

def get_smtp_port():
    """获取SMTP服务器端口"""
    return _config.getint('smtp', 'port')

def get_sender():
    """获取发件人邮箱"""
    return _config.get('smtp', 'sender')

def get_password():
    """获取发件人密码"""
    return _config.get('smtp', 'password')

def get_receivers():
    """获取收件人列表"""
    receivers = _config.get('smtp', 'receivers')
    return [r.strip() for r in receivers.split(',')]

def get_log_level():
    """获取日志级别"""
    return _config.get('log', 'level')

def get_log_format():
    """获取日志格式"""
    return _config.get('log', 'format')

def get_log_file():
    """获取日志文件路径"""
    return _config.get('log', 'file')

def get_log_max_size():
    """获取日志文件最大大小"""
    return _config.get('log', 'max_size')

def get_log_backup_count():
    """获取日志文件备份数量"""
    return _config.getint('log', 'backup_count')

def get_report_template():
    """获取报告模板路径"""
    return _config.get('report', 'template')

def get_report_output():
    """获取报告输出路径"""
    output = _config.get('report', 'output')
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    return output.format(timestamp=timestamp)