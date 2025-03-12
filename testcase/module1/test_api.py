# coding: utf-8
# author: chengmo
# description:

"""
API测试用例
"""

import unittest
from apis.interface1 import UserAPI
from comm import logger


class TestUserAPI(unittest.TestCase):
    """用户API测试类"""
    
    def setUp(self):
        """测试前置"""
        self.api = UserAPI("https://api.example.com")
    
    def test_login_success(self):
        """测试登录成功"""
        logger.info("开始测试: API登录成功")
        
        # 执行登录
        data, response = self.api.login("testuser", "password123")
        
        # 验证响应
        self.assertIsNotNone(response, "没有收到响应")
        self.assertEqual(response.status_code, 200, f"状态码不正确: {response.status_code}")
        
        # 验证数据
        self.assertIn("token", data, "响应中没有token字段")
        self.assertIsNotNone(data["token"], "token为空")
    
    def test_get_user_info(self):
        """测试获取用户信息"""
        logger.info("开始测试: 获取用户信息")
        
        # 先登录获取token
        login_data, _ = self.api.login("testuser", "password123")
        token = login_data.get("token")
        
        # 设置认证头
        self.api.set_header("Authorization", f"Bearer {token}")
        
        # 获取用户信息
        user_id = "12345"
        data, response = self.api.get_user_info(user_id)
        
        # 验证响应
        self.assertIsNotNone(response, "没有收到响应")
        self.assertEqual(response.status_code, 200, f"状态码不正确: {response.status_code}")
        
        # 验证数据
        self.assertIn("id", data, "响应中没有id字段")
        self.assertEqual(data["id"], user_id, "用户ID不匹配")
    
    def test_update_user_info(self):
        """测试更新用户信息"""
        logger.info("开始测试: 更新用户信息")
        
        # 先登录获取token
        login_data, _ = self.api.login("testuser", "password123")
        token = login_data.get("token")
        
        # 设置认证头
        self.api.set_header("Authorization", f"Bearer {token}")
        
        # 更新用户信息
        user_id = "12345"
        update_data = {
            "name": "New Name",
            "email": "new.email@example.com"
        }
        
        data, response = self.api.update_user_info(user_id, update_data)
        
        # 验证响应
        self.assertIsNotNone(response, "没有收到响应")
        self.assertEqual(response.status_code, 200, f"状态码不正确: {response.status_code}")
        
        # 验证数据
        self.assertIn("name", data, "响应中没有name字段")
        self.assertEqual(data["name"], update_data["name"], "更新后的名称不匹配")
        self.assertIn("email", data, "响应中没有email字段")
        self.assertEqual(data["email"], update_data["email"], "更新后的邮箱不匹配")

if __name__ == "__main__":
    unittest.main()