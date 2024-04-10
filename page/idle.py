from selenium.webdriver.common.by import By

from page.base_page import BasePage


class Idle(BasePage):
    def idle(self):
        element = self.find(By.ID, "com.kejian.huahua:id/tv_community")
        return element.text