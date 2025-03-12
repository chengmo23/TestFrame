# coding: utf-8
# author: chengmo
# description:

"""
基础页面类: UI自动化页面基类
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from comm import logger
from log.screen import ScreenCapture

class BasePage:
    """基础页面类"""
    
    def __init__(self, driver):
        """初始化基础页面"""
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.screen = ScreenCapture()
    
    def open(self, url):
        """打开页面"""
        logger.info(f"打开页面: {url}")
        self.driver.get(url)
    
    def find_element(self, locator):
        """查找元素"""
        try:
            element = self.wait.until(EC.presence_of_element_located(locator))
            return element
        except TimeoutException:
            logger.error(f"未找到元素: {locator}")
            self.screen.capture(f"element_not_found_{locator[1]}")
            return None
    
    def find_elements(self, locator):
        """查找多个元素"""
        try:
            elements = self.wait.until(EC.presence_of_all_elements_located(locator))
            return elements
        except TimeoutException:
            logger.error(f"未找到元素: {locator}")
            self.screen.capture(f"elements_not_found_{locator[1]}")
            return []
    
    def click(self, locator):
        """点击元素"""
        element = self.find_element(locator)
        if element:
            try:
                element.click()
                logger.info(f"点击元素: {locator}")
                return True
            except Exception as e:
                logger.error(f"点击元素失败: {locator}, 错误: {str(e)}")
                self.screen.capture(f"click_failed_{locator[1]}")
                return False
        return False
    
    def input_text(self, locator, text):
        """输入文本"""
        element = self.find_element(locator)
        if element:
            try:
                element.clear()
                element.send_keys(text)
                logger.info(f"输入文本: {locator}, 文本: {text}")
                return True
            except Exception as e:
                logger.error(f"输入文本失败: {locator}, 错误: {str(e)}")
                self.screen.capture(f"input_failed_{locator[1]}")
                return False
        return False
    
    def get_text(self, locator):
        """获取文本"""
        element = self.find_element(locator)
        if element:
            try:
                text = element.text
                logger.info(f"获取文本: {locator}, 文本: {text}")
                return text
            except Exception as e:
                logger.error(f"获取文本失败: {locator}, 错误: {str(e)}")
                self.screen.capture(f"get_text_failed_{locator[1]}")
                return None
        return None
    
    def is_element_present(self, locator, timeout=10):
        """判断元素是否存在"""
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
            return True
        except TimeoutException:
            return False
    
    def wait_for_element(self, locator, timeout=10):
        """等待元素出现"""
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
            return element
        except TimeoutException:
            logger.error(f"等待元素超时: {locator}")
            self.screen.capture(f"wait_timeout_{locator[1]}")
            return None