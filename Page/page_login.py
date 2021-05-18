from Base.base import Base
from Config import Login_config


class PageLogin(Base):
    # 选择密码登录
    def select_pwd_login(self):
        self.base_click(Login_config.pwd_login_click)

    # 输入用户名
    def input_username(self, value):
        self.base_input(Login_config.input_username, value)

    # 输入密码
    def input_pwd(self, value):
        self.base_input(Login_config.input_pwd, value)

    # 点击登录
    def click_login(self):
        self.base_click(Login_config.click_login)

    # 获取标题信息
    def get_title_info(self):
        return self.base_get_text(Login_config.title_info)

    # 获取当前url
    def get_url(self):
        return self.get_current_url()

