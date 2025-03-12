# coding: utf-8
# author: chengmo
# description:

"""
页面对象示例
"""

from selenium.webdriver.common.by import By
from page.base_page import BasePage

class LoginPage(BasePage):
    """登录页面类"""
    
    # 页面元素定位器
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login")
    ERROR_MESSAGE = (By.CLASS_NAME, "error-message")
    
    def __init__(self, driver):
        """初始化登录页面"""
        super().__init__(driver)
        self.url = "https://example.com/login"
    
    def open_login_page(self):
        """打开登录页面"""
        self.open(self.url)
    
    def login(self, username, password):
        """执行登录操作"""
        self.input_text(self.USERNAME_INPUT, username)
        self.input_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
    
    def get_error_message(self):
        """获取错误信息"""
        return self.get_text(self.ERROR_MESSAGE)
    
    def is_login_successful(self):
        """判断登录是否成功"""
        # 登录成功后通常会跳转到其他页面, 可以通过URL或特定元素判断
        return not self.is_element_present(self.ERROR_MESSAGE) and "dashboard" in self.driver.current_url