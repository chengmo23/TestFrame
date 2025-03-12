# coding: utf-8
# author: chengmo
# description:

"""
测试用例基类
"""

import unittest
import os
from datetime import datetime
from comm import logger
from comm.data import DataReader

class BaseTest(unittest.TestCase):
    """测试用例基类"""
    
    def setUp(self):
        """测试前置"""
        self.start_time = datetime.now()
        logger.info(f"开始测试: {self.__class__.__name__}.{self._testMethodName}")
    
    def tearDown(self):
        """测试后置"""
        end_time = datetime.now()
        duration = (end_time - self.start_time).total_seconds()
        logger.info(f"结束测试: {self.__class__.__name__}.{self._testMethodName}, 耗时: {duration}秒")
    
    def load_test_data(self, file_name):
        """加载测试数据"""
        # 获取当前测试模块所在目录
        current_dir = os.path.dirname(os.path.abspath(__file__))
        module_name = self.__class__.__module__.split('.')[-2]  # 获取模块名称
        
        # 构建测试数据文件路径
        data_file = os.path.join(current_dir, module_name, 'testdata', file_name)
        
        # 根据文件扩展名选择合适的读取方法
        if file_name.endswith('.json'):
            return DataReader.read_json(data_file)
        elif file_name.endswith('.yaml') or file_name.endswith('.yml'):
            return DataReader.read_yaml(data_file)
        elif file_name.endswith('.csv'):
            return DataReader.read_csv(data_file)
        elif file_name.endswith('.xml'):
            return DataReader.read_xml(data_file)
        else:
            raise ValueError(f"不支持的文件格式: {file_name}")
    
    def assert_json_contains(self, response, expected_keys):
        """断言JSON响应包含指定的键"""
        for key in expected_keys:
            self.assertIn(key, response, f"响应中缺少键: {key}")
    
    def assert_json_equals(self, actual, expected, ignore_keys=None):
        """断言JSON对象相等"""
        from comm.compare import Comparator
        
        is_equal, differences = Comparator.compare_json(actual, expected, ignore_keys)
        
        if not is_equal:
            diff_message = "\n".join(differences)
            self.fail(f"JSON对象不相等:\n{diff_message}")