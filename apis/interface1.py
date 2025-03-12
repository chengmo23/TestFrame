# coding: utf-8
# author: chengmo
# description:

"""
接口对象示例1
"""

from apis.base_api import BaseAPI

class UserAPI(BaseAPI):
    """用户接口类"""
    
    def __init__(self, base_url):
        """初始化用户接口"""
        super().__init__(base_url)
    
    def login(self, username, password):
        """用户登录"""
        data = {
            "username": username,
            "password": password
        }
        return self.post("/api/login", json_data=data)
    
    def get_user_info(self, user_id):
        """获取用户信息"""
        return self.get(f"/api/users/{user_id}")
    
    def update_user_info(self, user_id, user_data):
        """更新用户信息"""
        return self.put(f"/api/users/{user_id}", json_data=user_data)
    
    def delete_user(self, user_id):
        """删除用户"""
        return self.delete(f"/api/users/{user_id}")
    
    def register(self, user_data):
        """用户注册"""
        return self.post("/api/register", json_data=user_data)