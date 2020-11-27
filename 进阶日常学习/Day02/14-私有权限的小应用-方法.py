# 用户的登录和注册

class User:
    # 登录
    def login(self):
        # 1.接受用户名和密码
        # 2.验证
        # 3.登录操作
        self.__do_login()
        pass

    # 注册
    def register(self):
        # 1.接受注册的数据
        # 2.验证
        # 3.注册操作
        # 4.登录操作
        self.__do_login()
        pass

    def __do_login(self):
        # 登录操作
        pass

user = User()
user.login()
user.register()
# user.do_login()  # 这个方法不应该在外部被调用