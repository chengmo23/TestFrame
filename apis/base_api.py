# coding: utf-8
# author: chengmo
# description:

"""
基础API类: 接口自动化接口基类
"""

import requests
from comm import logger
from comm.encryption import Encryption

# TODO 抽象出基类, 派生客户端类
class BaseAPI:
    """基础API类"""
    
    def __init__(self, base_url):
        """初始化基础API"""
        self.base_url = base_url
        self.session = requests.Session()
        self.headers = {
            "Content-Type": "application/json",
            "User-Agent": "TestFrame/1.0"
        }
    
    def set_header(self, key, value):
        """设置请求头"""
        self.headers[key] = value
    
    def get(self, path, params=None, **kwargs):
        """发送GET请求"""
        url = self._build_url(path)
        logger.info(f"发送GET请求: {url}, 参数: {params}")
        
        try:
            response = self.session.get(
                url,
                params=params,
                headers=self.headers,
                **kwargs
            )
            return self._handle_response(response)
        except Exception as e:
            logger.error(f"GET请求异常: {url}, 错误: {str(e)}")
            return {"error": str(e)}, None
    
    def post(self, path, data=None, json_data=None, **kwargs):
        """发送POST请求"""
        url = self._build_url(path)
        log_data = data if data else json_data
        logger.info(f"发送POST请求: {url}, 数据: {log_data}")
        
        try:
            response = self.session.post(
                url,
                data=data,
                json=json_data,
                headers=self.headers,
                **kwargs
            )
            return self._handle_response(response)
        except Exception as e:
            logger.error(f"POST请求异常: {url}, 错误: {str(e)}")
            return {"error": str(e)}, None
    
    def put(self, path, data=None, json_data=None, **kwargs):
        """发送PUT请求"""
        url = self._build_url(path)
        log_data = data if data else json_data
        logger.info(f"发送PUT请求: {url}, 数据: {log_data}")
        
        try:
            response = self.session.put(
                url,
                data=data,
                json=json_data,
                headers=self.headers,
                **kwargs
            )
            return self._handle_response(response)
        except Exception as e:
            logger.error(f"PUT请求异常: {url}, 错误: {str(e)}")
            return {"error": str(e)}, None
    
    def delete(self, path, **kwargs):
        """发送DELETE请求"""
        url = self._build_url(path)
        logger.info(f"发送DELETE请求: {url}")
        
        try:
            response = self.session.delete(
                url,
                headers=self.headers,
                **kwargs
            )
            return self._handle_response(response)
        except Exception as e:
            logger.error(f"DELETE请求异常: {url}, 错误: {str(e)}")
            return {"error": str(e)}, None
    
    def _build_url(self, path):
        """构建完整URL"""
        if path.startswith("http"):
            return path
        return f"{self.base_url.rstrip('/')}/{path.lstrip('/')}"
    
    def _handle_response(self, response):
        """处理响应"""
        status_code = response.status_code
        
        try:
            if response.text:
                response_data = response.json()
            else:
                response_data = {}
        except ValueError:
            response_data = {"text": response.text}
        
        if status_code >= 400:
            logger.error(f"请求失败: 状态码 {status_code}, 响应: {response_data}")
        else:
            logger.info(f"请求成功: 状态码 {status_code}")
            
        return response_data, response
    
    def generate_signature(self, params, secret_key):
        """生成签名"""
        # 按照键排序
        sorted_params = sorted(params.items(), key=lambda x: x[0])
        
        # 构建签名字符串
        sign_str = "&".join([f"{key}={value}" for key, value in sorted_params])
        
        # 添加密钥
        sign_str += f"&key={secret_key}"
        
        # 计算签名
        return Encryption.md5(sign_str).upper()