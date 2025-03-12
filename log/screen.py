# coding: utf-8
# author: chengmo
# description:

"""
屏幕模块: UI自动化操作截图并放日志
"""

import os
from datetime import datetime
from comm import logger

# TODO 抽象出基类, 派生客户端类
class ScreenCapture:
    """屏幕截图类"""
    
    def __init__(self, output_dir="screenshots"):
        """初始化截图器"""
        self.output_dir = output_dir
        
        # 创建截图目录
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
    
    def capture(self, name=None):
        """捕获屏幕截图"""
        try:
            # 生成截图文件名
            if name is None:
                timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
                name = f"screenshot_{timestamp}.png"
            elif not name.endswith('.png'):
                name = f"{name}.png"
                
            # 截图路径
            screenshot_path = os.path.join(self.output_dir, name)
            
            # 捕获屏幕
            # TODO
            # screenshot = ImageGrab.grab()
            # screenshot.save(screenshot_path)
            
            logger.info(f"屏幕截图已保存: {screenshot_path}")
            return screenshot_path
        except Exception as e:
            logger.error(f"屏幕截图失败: {str(e)}")
            return None
    
    def capture_element(self, element, name=None):
        """捕获元素截图"""
        try:
            # 获取元素位置
            location = element.location
            size = element.size
            
            # 计算元素区域
            left = location['x']
            top = location['y']
            right = location['x'] + size['width']
            bottom = location['y'] + size['height']
            
            # 生成截图文件名
            if name is None:
                timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
                name = f"element_{timestamp}.png"
            elif not name.endswith('.png'):
                name = f"{name}.png"
                
            # 截图路径
            screenshot_path = os.path.join(self.output_dir, name)
            
            # 捕获屏幕并裁剪元素区域
            screenshot = ImageGrab.grab()
            element_image = screenshot.crop((left, top, right, bottom))
            element_image.save(screenshot_path)
            
            logger.info(f"元素截图已保存: {screenshot_path}")
            return screenshot_path
        except Exception as e:
            logger.error(f"元素截图失败: {str(e)}")
            return None