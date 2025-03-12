# coding: utf-8
# author: chengmo
# description:

"""
登录测试用例
"""

import unittest
from selenium import webdriver
from page.page_xxx import LoginPage
from comm import logger


class TestLogin(unittest.TestCase):
    """登录测试类"""
    
    def setUp(self):
        """测试前置"""
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.login_page = LoginPage(self.driver)
    
    def tearDown(self):
        """测试后置"""
        self.driver.quit()
    
    def test_login_success(self):
        """测试登录成功"""
        logger.info("开始测试: 登录成功")
        
        # 打开登录页面
        self.login_page.open_login_page()
        
        # 执行登录
        self.login_page.login("testuser", "password123")
        
        # 验证登录成功
        self.assertTrue(self.login_page.is_login_successful(), "登录失败")
    
    def test_login_failed_wrong_password(self):
        """测试登录失败 - 密码错误"""
        logger.info("开始测试: 登录失败 - 密码错误")
        
        # 打开登录页面
        self.login_page.open_login_page()
        
        # 执行登录
        self.login_page.login("testuser", "wrongpassword")
        
        # 验证登录失败
        self.assertFalse(self.login_page.is_login_successful(), "登录成功, 但预期应该失败")
        
        # 验证错误信息
        error_message = self.login_page.get_error_message()
        self.assertIn("密码错误", error_message, f"错误信息不符合预期: {error_message}")
    
    def test_login_failed_empty_username(self):
        """测试登录失败 - 用户名为空"""
        logger.info("开始测试: 登录失败 - 用户名为空")
        
        # 打开登录页面
        self.login_page.open_login_page()
        
        # 执行登录
        self.login_page.login("", "password123")
        
        # 验证登录失败
        self.assertFalse(self.login_page.is_login_successful(), "登录成功, 但预期应该失败")
        
        # 验证错误信息
        error_message = self.login_page.get_error_message()
        self.assertIn("用户名不能为空", error_message, f"错误信息不符合预期: {error_message}")

if __name__ == "__main__":
    unittest.main()