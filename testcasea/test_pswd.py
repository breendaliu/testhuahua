from time import sleep

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

from page.app import App
from page.base_page import BasePage


class TestPwsd:
        def setup(self):
            self.login = App().start().main().goto_test_login_password()

        def test_login_password(self):
            assert "首页" in self.login.login_pwsd()


            # # 手机号登录
            # self._driver.find_element(MobileBy.ID, "com.kejian.huahua:id/rl_phone_login").click()
            # # 点击密码登录
            # self._driver.find_element(MobileBy.ID, "com.kejian.huahua:id/tvPSwLogin").click()
            # 输入手机号码
            # self._driver.find_element(MobileBy.ID, "com.kejian.huahua:id/et_phone").send_keys("18500000015")
            # # 输入密码
            # self._driver.find_element(MobileBy.ID, "com.kejian.huahua:id/et_pswd").send_keys("123456")
            # # 点击登录
            # self._driver.find_element(MobileBy.ID, "com.kejian.huahua:id/rl_login_bg").click()
            # 断言，跳转到首页，获取位置权限
            # response = self._driver.find_element(MobileBy.ID, "com.android.permissioncontroller:id/permission_message")

