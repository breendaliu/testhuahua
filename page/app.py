import datetime

import pytest
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from page.base_page import BasePage
from page.main import Main


class App(BasePage):
    _package = "com.kejian.huahua"
    # app启动页activity
    _activity = ".SplashActivity"

    # app首页activity
    # _activity = ".MainActivity"

    def start(self):
        if self._driver is None:
            caps = {}
            caps["platformName"] = "android"
            caps["deviceName"] = "2NSDU20411000448"
            caps["appPackage"] = self._package
            caps["appActivity"] = self._activity
            caps["automationName"] = "uiAutomator2"
            # 在当前 session 下不会重置应用的状态,不清除缓存，如登录状态
            caps["noReset"] = True
            # 设置命令的操作时间
            caps["newCommandTimeout"] = 6000
            # caps['skipServerInstallation'] = True
            # caps['skipDeviceInitialization'] = True
            # 在使用 adb 启动应用之前，不要终止被测应用的进程。
            # caps["dontStopAppOnReset"] = True
            # 忽略软键盘，直接输入内容
            # caps['unicodeKeyboard'] = True
            # caps['resetKeyboard'] = True
            self._driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            self._driver.implicitly_wait(20)
        else:
            print(self._driver)
            self._driver.start_activity(self._package, self._activity)

        return self

    def restart(self):
        self._driver.close_app()
        self._driver.launch_app()
        return self

    # def stop(self):
    #     self._driver.quit()

    # def main(self) -> Main:
    #     return Main(self._driver)
    def main(self) -> Main:
        # todo: wait main page
        def wait_load(driver):
            print(datetime.datetime.now())
            source = self._driver.page_source

            if "我的" in source:
                return True
            if "同意" in source:
                return True
            if "image_cancel" in source:
                return True
            return False

        WebDriverWait(self._driver, 60).until(wait_load)
        return Main(self._driver)
