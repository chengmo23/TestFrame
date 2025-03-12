# coding: utf-8
# author: chengmo
# description:

"""
报告生成器: 存放测试报告
"""

import os
import json
from datetime import datetime
from jinja2 import Template
from conf import config
from comm import logger


class ReportGenerator:
    """报告生成器类"""
    
    def __init__(self):
        """初始化报告生成器"""
        self.template_path = config.get_report_template()
        self.output_path = config.get_report_output()
        
        # 创建报告目录
        output_dir = os.path.dirname(self.output_path)
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
    
    def generate(self, test_results):
        """生成测试报告"""
        try:
            # 读取模板
            with open(self.template_path, 'r', encoding='utf-8') as f:
                template_content = f.read()
            
            # 创建模板对象
            template = Template(template_content)
            
            # 准备报告数据
            report_data = {
                'title': '测试报告',
                'generated_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'summary': self._generate_summary(test_results),
                'results': test_results
            }
            
            # 渲染报告
            report_content = template.render(**report_data)
            
            # 保存报告
            with open(self.output_path, 'w', encoding='utf-8') as f:
                f.write(report_content)
                
            logger.info(f"测试报告已生成: {self.output_path}")
            return self.output_path
        except Exception as e:
            logger.error(f"生成测试报告失败: {str(e)}")
            return None
    
    def _generate_summary(self, test_results):
        """生成测试摘要"""
        total = len(test_results)
        passed = sum(1 for result in test_results if result['status'] == 'PASS')
        failed = sum(1 for result in test_results if result['status'] == 'FAIL')
        skipped = sum(1 for result in test_results if result['status'] == 'SKIP')
        
        pass_rate = (passed / total) * 100 if total > 0 else 0
        
        return {
            'total': total,
            'passed': passed,
            'failed': failed,
            'skipped': skipped,
            'pass_rate': f"{pass_rate:.2f}%",
            'duration': sum(result.get('duration', 0) for result in test_results)
        }

# 单例模式
_instance = None

def get_instance():
    """获取报告生成器实例"""
    global _instance
    if _instance is None:
        _instance = ReportGenerator()
    return _instance

def generate(test_results=None):
    """生成测试报告"""
    if test_results is None:
        # 如果没有提供测试结果, 则尝试从结果文件中读取
        try:
            with open('results.json', 'r', encoding='utf-8') as f:
                test_results = json.load(f)
        except Exception as e:
            logger.error(f"读取测试结果失败: {str(e)}")
            return None
    
    return get_instance().generate(test_results)