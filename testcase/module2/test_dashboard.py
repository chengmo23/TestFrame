# coding: utf-8
# author: chengmo
# description:

"""
仪表盘测试用例
"""

import unittest
from selenium import webdriver
from page.page_xxx import LoginPage
from page.page_xxx2 import DashboardPage
from comm import logger


class TestDashboard(unittest.TestCase):
    """仪表盘测试类"""
    
    def setUp(self):
        """测试前置"""
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.login_page = LoginPage(self.driver)
        self.dashboard_page = DashboardPage(self.driver)
        
        # 先登录
        self.login_page.open_login_page()
        self.login_page.login("testuser", "password123")
    
    def tearDown(self):
        """测试后置"""
        self.driver.quit()
    
    def test_welcome_message(self):
        """测试欢迎信息"""
        logger.info("开始测试: 欢迎信息")
        
        # 获取欢迎信息
        welcome_message = self.dashboard_page.get_welcome_message()
        
        # 验证欢迎信息
        self.assertIsNotNone(welcome_message, "没有获取到欢迎信息")
        self.assertIn("testuser", welcome_message, f"欢迎信息不包含用户名: {welcome_message}")
    
    def test_logout(self):
        """测试登出功能"""
        logger.info("开始测试: 登出功能")
        
        # 执行登出
        self.dashboard_page.logout()
        
        # 验证登出成功（应该回到登录页面）
        current_url = self.driver.current_url
        self.assertIn("login", current_url, f"登出后未跳转到登录页面: {current_url}")
    
    def test_go_to_profile(self):
        """测试跳转到个人资料页面"""
        logger.info("开始测试: 跳转到个人资料页面")
        
        # 跳转到个人资料页面
        self.dashboard_page.go_to_profile()
        
        # 验证跳转成功
        current_url = self.driver.current_url
        self.assertIn("profile", current_url, f"未跳转到个人资料页面: {current_url}")

if __name__ == "__main__":
    unittest.main()