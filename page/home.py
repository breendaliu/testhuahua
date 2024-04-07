from selenium.webdriver.common.by import By

from page.base_page import BasePage


class Home(BasePage):
    def home(self):
        self.steps("../data/home.yaml", "goto_home")
        element = self.find(By.ID, "com.kejian.huahua:id/tv_home")
        return element.text

    def store(self):
        self.steps("../data/home.yaml", "store")
        element = self.find(By.XPATH, "//*[contains(@text,'特色服务')]")
        return element.text

    def store_back(self):
        self.steps("../data/home.yaml", "store")
        self.steps("../data/home.yaml", "store_back")
        element = self.find(By.ID, "com.kejian.huahua:id/tv_home")
        return element.text

    def store_keyword(self):
        self.steps("../data/home.yaml", "store")
        self.steps("../data/home.yaml", "store_keyword")
        element = self.find(By.ID, "com.kejian.huahua:id/tv_search")
        return element.text