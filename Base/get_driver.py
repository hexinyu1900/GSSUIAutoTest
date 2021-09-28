from selenium import webdriver
from Config import Env_config
from Test.Business.business_login import LoginBusiness


class GetDriver:

    # 设置类属性
    driver = None

    # 获取driver
    @classmethod
    def get_driver(cls):
        if cls.driver is None:
            # 实例化浏览器
            cls.driver = webdriver.Chrome()
            # 最大化
            cls.driver.maximize_window()
            # 打开浏览器
            cls.driver.get(Env_config.url)
        return cls.driver

    # 退出driver
    @classmethod
    def quit_driver(cls):
        if cls.driver:
            cls.driver.quit()
            cls.driver = None


# case基类（其他业务）
class BaseCase(LoginBusiness):

    # 设置类属性
    driver = None

    # 获取driver
    @classmethod
    def case_forward(cls):
        if cls.driver is None:
            # 实例化浏览器
            cls.driver = webdriver.Chrome()
            # 最大化
            cls.driver.maximize_window()
            # 打开浏览器
            cls.driver.get(Env_config.url)
            # 登录
            cls.login = LoginBusiness(cls.driver)
            cls.login.pwd_login(18113748898, 12345678)
        return cls.driver

    # 退出driver
    @classmethod
    def quit_driver(cls):
        if cls.driver:
            cls.driver.quit()
            cls.driver = None

