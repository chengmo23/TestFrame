# coding: utf-8
# author: chengmo
# description:

"""
接口对象示例2
"""

from apis.base_api import BaseAPI

class ProductAPI(BaseAPI):
    """产品接口类"""
    
    def __init__(self, base_url):
        """初始化产品接口"""
        super().__init__(base_url)
    
    def get_products(self, page=1, size=10, category=None):
        """获取产品列表"""
        params = {
            "page": page,
            "size": size
        }
        
        if category:
            params["category"] = category
            
        return self.get("/api/products", params=params)
    
    def get_product_detail(self, product_id):
        """获取产品详情"""
        return self.get(f"/api/products/{product_id}")
    
    def create_product(self, product_data):
        """创建产品"""
        return self.post("/api/products", json_data=product_data)
    
    def update_product(self, product_id, product_data):
        """更新产品"""
        return self.put(f"/api/products/{product_id}", json_data=product_data)
    
    def delete_product(self, product_id):
        """删除产品"""
        return self.delete(f"/api/products/{product_id}")