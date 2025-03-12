# coding: utf-8
# author: chengmo
# description:

"""
另一个页面对象示例
"""

from selenium.webdriver.common.by import By
from page.base_page import BasePage

class DashboardPage(BasePage):
    """仪表盘页面类"""
    
    # 页面元素定位器
    WELCOME_MESSAGE = (By.CLASS_NAME, "welcome-message")
    LOGOUT_BUTTON = (By.ID, "logout")
    PROFILE_LINK = (By.XPATH, "//a[contains(text(), '个人资料')]")
    
    def __init__(self, driver):
        """初始化仪表盘页面"""
        super().__init__(driver)
        self.url = "https://example.com/dashboard"
    
    def open_dashboard(self):
        """打开仪表盘页面"""
        self.open(self.url)
    
    def get_welcome_message(self):
        """获取欢迎信息"""
        return self.get_text(self.WELCOME_MESSAGE)
    
    def logout(self):
        """执行登出操作"""
        self.click(self.LOGOUT_BUTTON)
    
    def go_to_profile(self):
        """跳转到个人资料页面"""
        self.click(self.PROFILE_LINK)