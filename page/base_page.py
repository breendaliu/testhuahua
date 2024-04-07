import json
import logging
import time
import yaml
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from page.handle_black import handle_black
from selenium.common.exceptions import NoSuchElementException


class BasePage:
    _driver: WebDriver
    _max_err_num = 10
    _error_num = 0
    _params = {}
    _black_list = [
        # 同意用户协议
        (By.ID, "com.kejian.huahua:id/tv_positive"),
        # 跳过启动页
        (By.ID, "com.kejian.huahua:id/iv_into"),
        # 同意隐私协议
        (By.ID, "com.kejian.huahua:id/iv_chose_state"),
        # 选择登录方式页面，同意用户协议
        (By.ID, "com.kejian.huahua:id/iv_chose_state"),
        # 获取位置权限
       # (By.ID, "com.android.permissioncontroller:id/permission_allow_always_button"),
        # (By.ID, "com.lbe.security.miui:id/permission_allow_foreground_only_button"),
        # 关闭首页弹窗
        (By.ID, "com.kejian.huahua:id/iv_del_img")
    ]

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    # 保存png文件，path是路径
    def screenshot(self, path):
        self._driver.save_screenshot(path)

    @handle_black
    def find(self, by, locator):
        logging.info("find")
        logging.info(locator)
        if locator is None:
            result = self._driver.find_element(*by)
        else:
            result = self._driver.find_element(by, locator)
        return result

    def finds(self, by, locator=None):
        logging.info("finds")
        logging.info(locator)
        if locator is None:
            result = self._driver.find_elements(*by)

        else:
            result = self._driver.find_elements(by, locator)
        return result

    # 隐式等待方法封装
    def set_implicitly_wait(self, second):
        self._driver.implicitly_wait(second)

    # 下滑x1=x2,y1<y2， 左滑x1>x2, y1=y2, 右滑x1<x2,y1=y2，上滑x1=x2,y1>y2
    def swipe(self, x1, y1, x2, y2):
        size = self._driver.get_window_size()
        # print(size)
        # time.sleep(3)
        self.set_implicitly_wait(20)
        for i in range(2):
            TouchAction(self._driver) \
                .long_press(x=size['width'] * x1, y=size['height'] * y1) \
                .move_to(x=size['width'] * x2, y=size['height'] * y2) \
                .release() \
                .perform()
        self.set_implicitly_wait(20)

    # 获取yaml文件中的数据，进行相应操作
    def steps(self, path, name):
        with open(path, encoding='utf-8') as f:
            steps = yaml.safe_load(f)[name]
        raw = json.dumps(steps)
        for key, value in self._params.items():
            raw = raw.replace("${" + key + "}", value)
        steps = json.loads(raw)
        for step in steps:
            if "action" in step.keys():
                action = step["action"]
                if "click" == action:
                    self.find(step["by"], step["locator"]).click()
                if "send" == action:
                    self.find(step["by"], step["locator"]).send_keys(step["value"])
                # if "len > 0" == action:
                #     eles = self.find(step["by"], step["locator"])
                #     return len(eles) > 0
                # 如果遇到点击搜索键的操作，调用press_keycode(66)方法
                if "press_keycode(66)" == action:
                    self._driver.press_keycode(66)
                # 如果遇到滑动屏幕的操作，调用swipe方法
                if "swipe" == action:
                    self.swipe(step["value1"], step["value2"], step["value3"], step["value4"])
                # 如果遇到等待，调用set_implicitly_wait方法
                if "set_implicitly_wait" == action:
                    self.set_implicitly_wait(step['value'])



