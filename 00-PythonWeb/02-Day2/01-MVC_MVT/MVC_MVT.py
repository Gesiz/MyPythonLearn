# MVC 的设计核心
# 解耦合 让不同的代码块之间降低耦合 增强代码的可扩展性 和可移植性

# M Model 主要 封装对数据库层的访问 对数据库进行 增 删 改 查 操作

# V View  用于 封装结果 生成页面展示的html 内容
# C Controller 用于接受请求 处理业务逻辑 与 Model 和 View 交互

# Django 框架遵循 MVC 设计
# M Model 与 MVC 中的M 功能相同 负责和数据库 交互 进行数据处理
# V View 与 MVC 中的C 功能相同 接受请求 处理业务 返回应答
# T Template 与MVC 中的 V 功能相同 负责构造返回的 html结果
