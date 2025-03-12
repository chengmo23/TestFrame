# coding: utf-8
# author: chengmo
# description:

"""
数据模块: 封装测试数据读取方法
"""

import json
import csv
import yaml
import xml.etree.ElementTree as ET

class DataReader:
    """数据读取类"""
    
    @staticmethod
    def read_json(file_path):
        """读取JSON文件"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"读取JSON文件失败: {str(e)}")
            return None
    
    @staticmethod
    def read_csv(file_path):
        """读取CSV文件"""
        try:
            data = []
            with open(file_path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    data.append(row)
            return data
        except Exception as e:
            print(f"读取CSV文件失败: {str(e)}")
            return None
    
    @staticmethod
    def read_yaml(file_path):
        """读取YAML文件"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return yaml.safe_load(f)
        except Exception as e:
            print(f"读取YAML文件失败: {str(e)}")
            return None
    
    @staticmethod
    def read_xml(file_path):
        """读取XML文件"""
        try:
            tree = ET.parse(file_path)
            return tree.getroot()
        except Exception as e:
            print(f"读取XML文件失败: {str(e)}")
            return None