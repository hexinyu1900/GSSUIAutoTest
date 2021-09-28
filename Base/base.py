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

    # 通过使用JS进行点击操作
    def js_click_element(self, loc):
        try:
            element = self.base_find_element(loc)
            self.driver.execute_script("arguments[0].click();", element)
            time.sleep(2)
        except Exception:
            raise ValueError('元素未找到！or 元素操作错误！')

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

    # 滚动条
    def base_scroll_bar(self):
        try:
            self.driver.execute_script("window.scrollTo(100,1000);")
        except Exception:
            raise Exception("滑动条出错啦！")

    # 获取表格表头
    def get_tr_th(self, loc, td_num):
        try:
            element = self.base_find_element(loc)
            return element.find_elements_by_css_selector('tr')[0].find_elements_by_css_selector('th')[td_num].text
        except Exception:
            raise ValueError('元素未找到！or 元素操作错误！')

    # 获取表格顶部数据
    def get_tr_td_desc(self, loc, td_num):
        try:
            time.sleep(2)
            element = self.base_find_element(loc)
            return element.find_elements_by_css_selector('tr')[0].find_elements_by_css_selector('td')[td_num].text
        except Exception:
            raise ValueError('元素未找到！or 元素操作错误！')

    # 点击列表顶部的按钮
    def click_tr_td_button_desc(self, loc, td_num, btn_num, ele_type='button'):
        try:
            time.sleep(2)
            element = self.base_find_element(loc)
            td = element.find_elements_by_css_selector('tr')[0].find_elements_by_css_selector('td')[td_num]
            # 兼容统计模块列表按钮为div的情况
            if ele_type == 'div':
                btn = td.find_elements_by_css_selector('div>div')[btn_num]
            else:
                btn = td.find_elements_by_css_selector('button')[btn_num]
            self.driver.execute_script("arguments[0].click();", btn)
        except Exception:
            raise ValueError('元素未找到！or 元素操作错误！')


