# coding: utf-8
# author: chengmo
# description:

"""
比较模块: 封装json比较, 用于接口测试结果比对
"""

import json
import difflib

class Comparator:
    """比较器类"""
    
    @staticmethod
    def compare_json(actual, expected, ignore_keys=None):
        """比较两个JSON对象"""
        if ignore_keys is None:
            ignore_keys = []
            
        if isinstance(actual, dict) and isinstance(expected, dict):
            return Comparator._compare_dict(actual, expected, ignore_keys)
        elif isinstance(actual, list) and isinstance(expected, list):
            return Comparator._compare_list(actual, expected, ignore_keys)
        else:
            return actual == expected, []
    
    @staticmethod
    def _compare_dict(actual, expected, ignore_keys):
        """比较两个字典"""
        differences = []
        
        # 检查缺失的键
        for key in expected:
            if key in ignore_keys:
                continue
                
            if key not in actual:
                differences.append(f"缺少键: {key}")
                continue
                
            if isinstance(expected[key], dict) and isinstance(actual[key], dict):
                _, sub_diff = Comparator._compare_dict(actual[key], expected[key], ignore_keys)
                differences.extend([f"{key}.{d}" for d in sub_diff])
            elif isinstance(expected[key], list) and isinstance(actual[key], list):
                _, sub_diff = Comparator._compare_list(actual[key], expected[key], ignore_keys)
                differences.extend([f"{key}[{d}]" for d in sub_diff])
            elif actual[key] != expected[key]:
                differences.append(f"值不同 - 键: {key}, 期望: {expected[key]}, 实际: {actual[key]}")
        
        return len(differences) == 0, differences
    
    @staticmethod
    def _compare_list(actual, expected, ignore_keys):
        """比较两个列表"""
        differences = []
        
        if len(actual) != len(expected):
            differences.append(f"列表长度不同 - 期望: {len(expected)}, 实际: {len(actual)}")
            
        for i, (act_item, exp_item) in enumerate(zip(actual, expected)):
            if isinstance(act_item, dict) and isinstance(exp_item, dict):
                _, sub_diff = Comparator._compare_dict(act_item, exp_item, ignore_keys)
                differences.extend([f"{i}.{d}" for d in sub_diff])
            elif isinstance(act_item, list) and isinstance(exp_item, list):
                _, sub_diff = Comparator._compare_list(act_item, exp_item, ignore_keys)
                differences.extend([f"{i}[{d}]" for d in sub_diff])
            elif act_item != exp_item:
                differences.append(f"值不同 - 索引: {i}, 期望: {exp_item}, 实际: {act_item}")
        
        return len(differences) == 0, differences
    
    @staticmethod
    def generate_diff_report(actual, expected):
        """生成差异报告"""
        actual_str = json.dumps(actual, indent=2, ensure_ascii=False)
        expected_str = json.dumps(expected, indent=2, ensure_ascii=False)
        
        diff = difflib.unified_diff(
            expected_str.splitlines(),
            actual_str.splitlines(),
            fromfile='预期结果',
            tofile='实际结果',
            lineterm=''
        )
        
        return '\n'.join(diff)