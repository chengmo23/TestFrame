# coding: utf-8
# author: chengmo
# description:

"""
测试套件
"""

import os
import unittest
from comm import logger


def discover_tests(start_dir=None, pattern="test_*.py"):
    """发现测试用例"""
    if start_dir is None:
        # 默认使用当前目录
        start_dir = os.path.dirname(os.path.abspath(__file__))
        
    logger.info(f"开始发现测试用例: {start_dir}")
    
    # 使用unittest的discover方法发现测试用例
    suite = unittest.defaultTestLoader.discover(start_dir, pattern=pattern)
    
    # 统计测试用例数量
    case_count = count_test_cases(suite)
    logger.info(f"发现测试用例: {case_count}个")
    
    return suite

def count_test_cases(suite):
    """统计测试用例数量"""
    count = 0
    for test in suite:
        if isinstance(test, unittest.TestSuite):
            count += count_test_cases(test)
        else:
            count += 1
    return count

def create_suite_by_module(module_name):
    """根据模块名创建测试套件"""
    start_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), module_name)
    
    if not os.path.exists(start_dir):
        logger.error(f"模块不存在: {module_name}")
        return unittest.TestSuite()
    
    logger.info(f"为模块创建测试套件: {module_name}")
    return discover_tests(start_dir)

def create_suite_by_case(module_name, case_name):
    """根据模块名和用例名创建测试套件"""
    suite = unittest.TestSuite()
    
    try:
        # 导入测试模块
        module_path = f"testcase.{module_name}.{case_name}"
        __import__(module_path)
        
        # 获取所有测试用例
        module = __import__(module_path, fromlist=["*"])
        for name in dir(module):
            obj = getattr(module, name)
            if isinstance(obj, type) and issubclass(obj, unittest.TestCase) and obj != unittest.TestCase:
                suite.addTest(unittest.makeSuite(obj))
                
        logger.info(f"为用例创建测试套件: {module_name}.{case_name}")
    except (ImportError, AttributeError) as e:
        logger.error(f"创建测试套件失败: {str(e)}")
    
    return suite

def run_tests(suite, report=True):
    """运行测试套件"""
    from report import report_generator
    
    logger.info("开始运行测试")
    
    # 创建测试结果收集器
    result = unittest.TestResult()
    
    # 运行测试
    suite.run(result)
    
    # 输出测试结果
    logger.info(f"测试完成: 总数={result.testsRun}, 成功={result.testsRun - len(result.failures) - len(result.errors)}, 失败={len(result.failures)}, 错误={len(result.errors)}")
    
    # 处理失败的测试
    if result.failures:
        logger.error("失败的测试:")
        for test, traceback in result.failures:
            logger.error(f"- {test}")
            logger.debug(traceback)
    
    # 处理错误的测试
    if result.errors:
        logger.error("错误的测试:")
        for test, traceback in result.errors:
            logger.error(f"- {test}")
            logger.debug(traceback)
    
    # 生成测试报告
    if report:
        # 转换测试结果为报告格式
        test_results = []
        
        # 处理成功的测试
        for test in result.successes:
            test_results.append({
                "name": str(test),
                "status": "PASS",
                "message": "",
                "duration": 0  # 这里需要改进, 记录每个测试的实际耗时
            })
        
        # 处理失败的测试
        for test, traceback in result.failures:
            test_results.append({
                "name": str(test),
                "status": "FAIL",
                "message": traceback,
                "duration": 0
            })
        
        # 处理错误的测试
        for test, traceback in result.errors:
            test_results.append({
                "name": str(test),
                "status": "ERROR",
                "message": traceback,
                "duration": 0
            })
        
        # 生成报告
        report_path = report_generator.generate(test_results)
        logger.info(f"测试报告已生成: {report_path}")
    
    return result