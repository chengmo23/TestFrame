# coding: utf-8
# author: chengmo
# description:

"""
主程序文件: 扫描用例、执行用例、输出报告、发送邮件
"""

import argparse
from conf import config
from comm import logger as log
from report import report_generator
from comm.email import send_report

def parse_args():
    """解析命令行参数"""
    parser = argparse.ArgumentParser(description="测试框架")
    parser.add_argument("-m", "--module", help="指定要执行的测试模块")
    parser.add_argument("-c", "--case", help="指定要执行的测试用例")
    parser.add_argument("-r", "--report", action="store_true", help="生成测试报告")
    parser.add_argument("-e", "--email", action="store_true", help="发送邮件报告")
    return parser.parse_args()

def scan_testcases(module=None):
    """扫描测试用例"""
    log.info("开始扫描测试用例")
    # TODO 扫描测试用例
    pass

def run_testcases(cases):
    """执行测试用例"""
    log.info("开始执行测试用例")
    # TODO 执行测试用例
    pass

def generate_report():
    """生成测试报告"""
    log.info("开始生成测试报告")
    # 调用报告生成模块
    report_generator.generate()

def send_report_email():
    """发送测试报告邮件"""
    log.info("开始发送测试报告邮件")
    # 调用邮件发送模块
    send_report()

def main():
    """主函数"""
    args = parse_args()
    
    # 初始化配置
    config.init()
    
    # 初始化日志
    log.init()
    
    # 扫描测试用例
    cases = scan_testcases(args.module)
    
    # 执行测试用例
    results = run_testcases(cases)
    
    # 生成报告
    if args.report:
        generate_report()
    
    # 发送邮件
    if args.email:
        send_report_email()


if __name__ == "__main__":
    main()
