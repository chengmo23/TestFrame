# coding: utf-8
# author: chengmo
# description:

"""
加密模块: 封装加密方法, 用于接口签名等
"""

import hashlib
import base64
import hmac
import binascii
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

class Encryption:
    """加密类"""
    
    @staticmethod
    def md5(text):
        """MD5加密"""
        if isinstance(text, str):
            text = text.encode('utf-8')
        return hashlib.md5(text).hexdigest()
    
    @staticmethod
    def sha1(text):
        """SHA1加密"""
        if isinstance(text, str):
            text = text.encode('utf-8')
        return hashlib.sha1(text).hexdigest()
    
    @staticmethod
    def sha256(text):
        """SHA256加密"""
        if isinstance(text, str):
            text = text.encode('utf-8')
        return hashlib.sha256(text).hexdigest()
    
    @staticmethod
    def base64_encode(text):
        """Base64编码"""
        if isinstance(text, str):
            text = text.encode('utf-8')
        return base64.b64encode(text).decode('utf-8')
    
    @staticmethod
    def base64_decode(text):
        """Base64解码"""
        return base64.b64decode(text).decode('utf-8')
    
    @staticmethod
    def hmac_sha256(key, message):
        """HMAC-SHA256加密"""
        if isinstance(key, str):
            key = key.encode('utf-8')
        if isinstance(message, str):
            message = message.encode('utf-8')
        return hmac.new(key, message, hashlib.sha256).hexdigest()
    
    @staticmethod
    def aes_encrypt(text, key, iv):
        """AES加密"""
        if isinstance(text, str):
            text = text.encode('utf-8')
        if isinstance(key, str):
            key = key.encode('utf-8')
        if isinstance(iv, str):
            iv = iv.encode('utf-8')
            
        cipher = AES.new(key, AES.MODE_CBC, iv)
        encrypted = cipher.encrypt(pad(text, AES.block_size))
        return binascii.b2a_hex(encrypted).decode('utf-8')
    
    @staticmethod
    def aes_decrypt(encrypted_text, key, iv):
        """AES解密"""
        if isinstance(encrypted_text, str):
            encrypted_text = binascii.a2b_hex(encrypted_text)
        if isinstance(key, str):
            key = key.encode('utf-8')
        if isinstance(iv, str):
            iv = iv.encode('utf-8')
            
        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypted = unpad(cipher.decrypt(encrypted_text), AES.block_size)
        return decrypted.decode('utf-8')