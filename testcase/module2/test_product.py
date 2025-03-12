# coding: utf-8
# author: chengmo
# description:

"""
产品测试用例
"""

import unittest
from apis.interface2 import ProductAPI
from comm import logger


class TestProductAPI(unittest.TestCase):
    """产品API测试类"""
    
    def setUp(self):
        """测试前置"""
        self.api = ProductAPI("https://api.example.com")
        
        # 设置认证头（假设已经获取了token）
        self.api.set_header("Authorization", "Bearer test_token")
    
    def test_get_products(self):
        """测试获取产品列表"""
        logger.info("开始测试: 获取产品列表")
        
        # 获取产品列表
        data, response = self.api.get_products(page=1, size=10)
        
        # 验证响应
        self.assertIsNotNone(response, "没有收到响应")
        self.assertEqual(response.status_code, 200, f"状态码不正确: {response.status_code}")
        
        # 验证数据
        self.assertIn("items", data, "响应中没有items字段")
        self.assertIsInstance(data["items"], list, "items不是列表")
        self.assertIn("total", data, "响应中没有total字段")
    
    def test_get_product_detail(self):
        """测试获取产品详情"""
        logger.info("开始测试: 获取产品详情")
        
        # 获取产品详情
        product_id = "12345"
        data, response = self.api.get_product_detail(product_id)
        
        # 验证响应
        self.assertIsNotNone(response, "没有收到响应")
        self.assertEqual(response.status_code, 200, f"状态码不正确: {response.status_code}")
        
        # 验证数据
        self.assertIn("id", data, "响应中没有id字段")
        self.assertEqual(data["id"], product_id, "产品ID不匹配")
        self.assertIn("name", data, "响应中没有name字段")
        self.assertIn("price", data, "响应中没有price字段")
    
    def test_create_product(self):
        """测试创建产品"""
        logger.info("开始测试: 创建产品")
        
        # 创建产品
        product_data = {
            "name": "测试产品",
            "price": 99.99,
            "description": "这是一个测试产品",
            "category": "测试"
        }
        
        data, response = self.api.create_product(product_data)
        
        # 验证响应
        self.assertIsNotNone(response, "没有收到响应")
        self.assertEqual(response.status_code, 201, f"状态码不正确: {response.status_code}")
        
        # 验证数据
        self.assertIn("id", data, "响应中没有id字段")
        self.assertIn("name", data, "响应中没有name字段")
        self.assertEqual(data["name"], product_data["name"], "产品名称不匹配")
        self.assertIn("price", data, "响应中没有price字段")
        self.assertEqual(float(data["price"]), product_data["price"], "产品价格不匹配")

if __name__ == "__main__":
    unittest.main()