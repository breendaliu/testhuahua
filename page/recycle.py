from selenium.webdriver.common.by import By

from page.base_page import BasePage


class Recycle(BasePage):
    def recycle(self):
        element = self.find(By.ID, "com.kejian.huahua:id/tv_wallet")
        return element.text