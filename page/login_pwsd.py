from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

from page.base_page import BasePage


class LoginPwsd(BasePage):

    # 使用密码登录，使用login_pswd.yaml文件中的定位及value值，进行操作
    def login_pwsd(self):
        # 手机号登录
        # self._driver.find_element(MobileBy.ID, "com.kejian.huahua:id/rl_phone_login").click()
        # # 点击密码登录
        # self._driver.find_element(MobileBy.ID, "com.kejian.huahua:id/tvPSwLogin").click()
        # 手机号登录
        #self._driver.find_element(MobileBy.ID, "com.kejian.huahua:id/rl_phone_login").click()
        # # 点击密码登录
        #self._driver.find_element(MobileBy.ID, "com.kejian.huahua:id/tvPSwLogin").click()
        # 断言
        # element = self._driver.find_element(By.ID, "com.kejian.huahua:id/tv_home")
        # self.steps("..data/login_pswd.yaml", "login_pswd")
        element = self.find(By.ID, "com.kejian.huahua:id/tv_home")
        return element.text
