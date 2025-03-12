# TestFrame 测试框架

这是一个基于Python的自动化测试框架，支持UI自动化测试和API接口测试。

## 目录结构
```tree
TestFrame/
├── apis/                       # API接口模块
│   ├── base_api.py             # 接口基类
│   ├── interface1.py           # 接口对象1
│   └── interface2.py           # 接口对象2
├── comm/                       # 通用模块
│   ├── data.py                 # 数据处理
│   ├── email.py                # 邮件发送
│   ├── compare.py              # 比较工具
│   └── encryption.py           # 加密工具
├── conf/                       # 配置模块
│   ├── config.ini              # 配置文件
│   └── config.py               # 配置读取
├── log/                        # 日志模块
│   ├── logger.py               # 日志工具
│   └── screen.py               # 截图工具
├── page/                       # 页面模块
│   ├── base_page.py            # 页面基类
│   ├── page_xxx.py             # 页面对象1
│   └── page_xxx2.py            # 页面对象2
├── report/                     # 报告模块
│   └── report_generator.py     # 报告生成器
├── templates/                  # 模板目录
│   └── report_template.html    # 报告模板
├── testcase/                   # 测试用例
│   ├── base_test.py            # 测试基类
│   ├── test_suite.py           # 测试套件
│   ├── module1/                # 模块1
│   │   ├── test_login.py       # 登录测试
│   │   ├── test_api.py         # API测试
│   │   └── testdata/           # 测试数据
│   └── module2/                # 模块2
│       ├── test_product.py     # 产品测试
│       ├── test_dashboard.py   # 仪表盘测试
│       └── testdata/           # 测试数据
└── main.py                     # 主程序
```

# TODO
1. 从 unittest 切换到 pytest
2. 扫描测试用例
3. 执行测试用例
4. 邮件添加附件
5. 截图需要优化, 抽象出基类, 派生客户端类
