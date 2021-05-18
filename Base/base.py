import time
from selenium.webdriver.support.wait import WebDriverWait
from Tools.get_log import GetLogger

log = GetLogger().get_logger()


class Base:
    # 初始化方法
    def __init__(self, driver):
        self.driver = driver

    # 查找元素
    def base_find_element(self, loc, timeout=2, poll=0.5):
        log.info("正在查找元素{}".format(loc))
        element, num = loc[:2], loc[-1]
        try:
            el = WebDriverWait(self.driver,
                               timeout=timeout,
                               poll_frequency=poll).until(lambda x: x.find_elements(*element))[num]
        except Exception:
            raise Exception("元素定位错误！")
        else:
            return el

    # 输入
    def base_input(self, loc, value):
        element = self.base_find_element(loc)
        try:
            log.info("正在给元素{}输入内容".format(loc))
            element.send_keys(value)
        except Exception:
            raise Exception("输入错误！")

    # 清空
    def base_clear(self, loc):
        element = self.base_find_element(loc)
        try:
            log.info("清空元素{}内容".format(loc))
            element.clear()
        except Exception:
            raise Exception("清空错误！")

    # 点击
    def base_click(self, loc):
        element = self.base_find_element(loc)
        try:
            log.info("正在点击元素{}".format(loc))
            element.click()
        except Exception:
            raise Exception("点击错误！")

    # 获取文字信息
    def base_get_text(self, loc):
        element = self.base_find_element(loc)
        try:
            log.info("正在获取元素{}信息".format(loc))
            return element.text
        except Exception:
            raise Exception("获取文字信息错误！")

    # 获取当前页面URL
    def get_current_url(self):
        time.sleep(2)
        return self.driver.current_url

    # 截图
    def base_screenshot(self):
        try:
            self.driver.get_screenshot_as_file("E:\GSSUIAutoTest\Image\{}.png".format(time.strftime("%Y_%m_%d %H_%M_%S")))
        except Exception:
            raise Exception("截图失败！")


