# coding: utf-8
# author: chengmo
# description:

"""
邮件模块: 封装邮件, 用于发送测试报告
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from conf import config

class EmailSender:
    """邮件发送类"""
    
    def __init__(self):
        """初始化邮件发送器"""
        self.smtp_server = config.get_smtp_server()
        self.smtp_port = config.get_smtp_port()
        self.sender = config.get_sender()
        self.password = config.get_password()
        self.receivers = config.get_receivers()
    
    def create_message(self, subject, content, attachments=None):
        """创建邮件消息"""
        message = MIMEMultipart()
        message['From'] = self.sender
        message['To'] = ','.join(self.receivers)
        message['Subject'] = subject
        
        # 添加正文
        message.attach(MIMEText(content, 'html', 'utf-8'))
        
        # 添加附件
        if attachments:
            for attachment in attachments:
                # TODO 添加附件
                pass
                
        return message
    
    def send(self, message):
        """发送邮件"""
        try:
            smtp = smtplib.SMTP(self.smtp_server, self.smtp_port)
            smtp.starttls()
            smtp.login(self.sender, self.password)
            smtp.sendmail(self.sender, self.receivers, message.as_string())
            smtp.quit()
            return True
        except Exception as e:
            print(f"发送邮件失败: {str(e)}")
            return False

def send_report():
    """发送测试报告"""
    sender = EmailSender()
    message = sender.create_message(
        subject="测试报告",
        content="请查看附件中的测试报告",
        attachments=["report.html"]
    )
    return sender.send(message)